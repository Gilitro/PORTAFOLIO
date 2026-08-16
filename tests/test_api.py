from fastapi.testclient import TestClient
from src.api.main import app
from datetime import datetime

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_endpoint():
    payload = {
        "symbol": "EURUSD",
        "timestamp": datetime.now().isoformat(),
        "sma_20": 1.0500,
        "rsi_14": 55.0,
        "macd": 0.001,
        "atr_14": 0.002
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "action" in data
    assert data["action"] in ["BUY", "SELL", "HOLD"]
