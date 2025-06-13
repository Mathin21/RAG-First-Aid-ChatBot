from fastapi import FastAPI, Query
from dotenv import load_dotenv
import json

load_dotenv()

from src.database import setup_db_index
from src.retrieval import web_search, format_web_results
from src.generator import generate_prompt, generate_response

index = setup_db_index()
retriever = index.as_retriever(similarity_top_k=2)

app = FastAPI(title="RAG First-Aid Chatbot")

@app.get("/ask")
def ask(query: str = Query(..., description="Medical emergency description")):
    local_context = "\n".join([n.get_content() for n in retriever.retrieve(query)])
    web_context = format_web_results(web_search(query))
    prompt = generate_prompt(query, web_context, local_context)
    answer_raw = generate_response(prompt)

    try:
        answer = json.loads(answer_raw)
    except Exception:
        answer = {"error": "Failed to parse structured response", "raw": answer_raw}

    return {"query": query, **answer}
