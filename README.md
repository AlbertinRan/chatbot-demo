# AI Chatbot Demo 🤖

This is a **demo version** of a professional AI chatbot system developed by **Randriamiharisoa Nomenjanahary Albertin**.  
It can run locally using the **Mistral LLM** (no API key required) for testing and demonstration purposes.

---

## Features
- Intelligent chatbot capable of responding to professional queries
- Runs locally using **Mistral 7B** or similar LLM
- Handles conversation flow and context for simple demos
- Fully offline (optional GPU acceleration if available)
- Easy to integrate with web apps or GUI frameworks like FastAPI or PyQt5

---

## Tech Stack
- **Language:** Python  
- **Libraries:** `transformers`, `torch`, `FastAPI`, `pydantic`  
- **Framework:** FastAPI (for REST API)

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

> **Note:** Installing `torch` can take some time depending on your system.  
> You may choose CPU-only or GPU installation as needed:
>
> CPU-only:
> ```bash
> pip install torch --index-url https://download.pytorch.org/whl/cpu
> ```
>
> GPU (CUDA 11.8):
> ```bash
> pip install torch --index-url https://download.pytorch.org/whl/cu118
> ```

4. Run the demo API:

```bash
uvicorn main:app --reload
```

5. Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

You can test the `/chat` endpoint directly from Swagger UI.

---

## Usage / Example

1. Send a POST request to `/chat` with JSON payload:

```json
{
  "message": "Hello, how are you?"
}
```

2. Response:

```json
{
  "response": "Hello! I am your AI assistant. How can I help you today?"
}
```

3. Works offline using Mistral locally; if GPU is available, responses are faster.

---

## Author

**Randriamiharisoa Nomenjanahary Albertin**

* 📍 Madagascar
* 📞 +261 34 26 376 11
* 📧 [ndriamihary.28@gmail.com](mailto:ndriamihary.28@gmail.com)
* 🌐 GitHub: [AlbertinRan](https://github.com/AlbertinRan)

---

## Notes

* This is a **demo version** for showcasing AI skills.
* No sensitive data is stored.
* Can be extended for integration with CRM or ERP systems.
* Mistral model can be swapped for OpenAI API if you have a valid API key.

---