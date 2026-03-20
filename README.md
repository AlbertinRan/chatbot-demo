# AI Chatbot Demo 🤖

This is a **demo version** of a professional AI chatbot system developed by **Randriamiharisoa Nomenjanahary Albertin**.  
It uses the **Mistral AI API** to generate intelligent responses in real time.

---

## Features
- Intelligent chatbot capable of responding to professional queries
- Real-time responses using **Mistral LLM API**
- Lightweight (no heavy local model required)
- Built with FastAPI for high performance
- Easy integration with web or mobile applications
- Environment-based configuration using `.env`

---

## Tech Stack
- **Language:** Python  
- **Framework:** FastAPI  
- **AI:** Mistral API  
- **Libraries:** `requests`, `pydantic`, `python-dotenv`  

---

## Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/AlbertinRan/chatbot-demo.git
cd chatbot-demo
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the environment:

* **Windows PowerShell:**
```bash
.\venv\Scripts\Activate.ps1
```

* **Linux / Mac:**
```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

Create a `.env` file:

```env
API_KEY=your_mistral_api_key_here
```

5. Run the API server:

```bash
uvicorn main:app --reload
```

6. Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Usage

### 🔹 Example Request

**POST /chat**

```json
{
  "message": "Hello, how are you?"
}
```

---

### 🔹 Example Response

```json
{
  "response": "Hello! I'm doing well. How can I assist you today?"
}
```

---

## Author

**Randriamiharisoa Nomenjanahary Albertin**

* 📍 Madagascar
* 📞 +261 34 26 376 11
* 📧 [ndriamihary.28@gmail.com](mailto:ndriamihary.28@gmail.com)
* 🌐 GitHub: https://github.com/AlbertinRan

---

## Notes

* This project uses the **Mistral API**, so an internet connection is required.
* The `.env` file is not included for security reasons.
* This is a **demo backend**, not production-ready.
* Can be extended with authentication, database, and conversation memory.

---

## Future Improvements

* Add conversation memory (chat history)
* Integrate database (PostgreSQL / MongoDB)
* Add frontend interface (React / HTML)
* Deploy with Docker

---