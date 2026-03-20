from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Charger variables d'environnement
load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY is missing! Add it in .env file.")

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "AI Chatbot API running with Mistral API"}


@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message

    try:
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral-small",
                "messages": [
                    {"role": "user", "content": user_message}
                ]
            },
            timeout=10
        )

        # Vérification erreur API
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Mistral API error: {response.text}"
            )

        data = response.json()
        reply = data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request failed: {e}")
    except (KeyError, IndexError):
        raise HTTPException(status_code=500, detail="Invalid response from Mistral API")

    return {"response": reply}