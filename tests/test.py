from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_query_endpoint():
    response = client.post("/query", json={"query": "Sample query", "top_k": 3})
    assert response.status_code == 200
    data = response.json()
    assert "prompt" in data
    assert "questions" in data
    assert len(data["prompt"]) == 3
    assert len(data["questions"]) == 3
