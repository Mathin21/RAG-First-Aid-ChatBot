import os
import requests

def web_search(query, k=3):
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }
    payload = {"q": query, "num": k}
    response = requests.post("https://google.serper.dev/search", headers=headers, json=payload)
    return response.json().get("organic", [])[:k]

def format_web_results(results):
    return "\n".join(f"{r['title']}: {r['snippet']}\nURL: {r['link']}" for r in results)
