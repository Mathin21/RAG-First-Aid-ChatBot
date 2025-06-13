from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_ask():
    response = client.get("/ask", params={"query": "shaky and sweating, glucose 55"})
    assert response.status_code == 200
    assert "response" in response.json()
