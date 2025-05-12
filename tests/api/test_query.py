from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_query_success():
    payload = {
        "query": "What is the capital of France?",
        "top_k": 3
    }
    response = client.post("/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "excerpts" in data
    assert isinstance(data["excerpts"], list)


def test_query_empty_input():
    payload = {
        "query": "",
        "top_k": 3
    }
    response = client.post("/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["excerpts"], list)

def test_query_invalid_topk():
    payload = {
        "query": "Some query",
        "top_k": -1
    }
    response = client.post("/query", json=payload)
    assert response.status_code == 422  # Validation error for negative top_k
