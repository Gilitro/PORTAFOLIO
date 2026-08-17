from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_signals():
    response = client.get("/signals")
    assert response.status_code == 200
    assert "signals" in response.json()

def test_predict():
    payload = {"feature1": 0.5, "feature2": 1.2, "feature3": -0.3}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
