# 🩺 RAG-Powered First-Aid Chatbot

This project is a **Retrieval-Augmented Generation (RAG)** chatbot for **Diabetes, Cardiac, and Renal emergencies**. It combines:
- 🧠 Local semantic knowledge (from curated CSV)
- 🌐 Live web search (Serper.dev)
- 💬 GPT-4 for natural language responses

---

## 🚀 Features

- First-aid triage for serious medical symptoms
- Uses OpenAI GPT-4 and real-time Serper.dev search
- Structured, JSON-based, easy-to-render output
- Built with FastAPI, easily extendable to Streamlit or UI

---

## Flowchart

![Render Flow](render-flowchart.png)

--

## 🛠 Setup

### 1. Clone the repo

```bash
git clone https://github.com/Mathin21/RAG-First-Aid-ChatBot.git
cd RAG-First-Aid-ChatBot
```

### 2. Create .env

```bash
cp .env.example .env
```
✏️ Edit .env and add your actual API keys:
```bash
OPENAI_API_KEY="your-openai-key"
SERPER_API_KEY="your-serper-key"
```

### 3. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

### 4. Install requirements

```bash
pip install -r requirements.txt
```

### 5. Load SQLite DB

```bash
python load_data.py
```
✅ This creates diseases.db from the file Assignment Data Base.csv.

### 6. Start the FastAPI server

```bash
uvicorn src.app:app --reload
```

Visit:

📘 **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Or test directly using `curl`:

---

### 📬 Example Usage (with curl)

```bash
curl "http://127.0.0.1:8000/ask?query=My glucose is 55 and I'm shaky"
```

### 🔐 Environment Variables

| Variable         | Description                             |
|------------------|-----------------------------------------|
| `OPENAI_API_KEY` | Your OpenAI key (GPT-4 access required) |
| `SERPER_API_KEY` | Your Serper.dev key                     |

---

### 🧠 Sample Test Queries

- "I’m sweating, shaky, and my glucometer reads 55 mg/dL—what should I do right now?"
- "My diabetic father just became unconscious; we think his sugar crashed."
- "Crushing chest pain shooting down my left arm—do I chew aspirin first or call an ambulance?"
- "CKD patient with a potassium level of 6.1 mmol/L—what emergency measures can we start right away?"

### 🧑‍⚕️ Disclaimer

⚠️ This chatbot is for educational and informational purposes only and **does not replace professional medical advice**. Always consult a doctor for emergency care.

### 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software with proper attribution.

MIT © [Mathin21](https://github.com/Mathin21)

