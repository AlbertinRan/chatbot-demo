    
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

# Charger le modèle Mistral (par exemple gpt4all ou Mistral 7B)
MODEL_NAME = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16)
model.eval()

@app.get("/")
def home():
    return {"message": "AI Chatbot API running with Mistral"}

@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message

    # Préparer l'input
    inputs = tokenizer(user_message, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    # Générer la réponse
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=150)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"response": reply}