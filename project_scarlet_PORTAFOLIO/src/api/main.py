from fastapi import FastAPI
from .schemas import Signal, FeatureInput, Prediction

app = FastAPI(
    title="Project Scarlet API",
    description="API de ejemplo para demostración de habilidades",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/signals")
def get_signals():
    return {
        "signals": [
            {"id": 1, "symbol": "EURUSD", "direction": "BUY", "probability": 0.75, "timestamp": "2024-01-01T10:00:00Z"},
            {"id": 2, "symbol": "GBPUSD", "direction": "SELL", "probability": 0.68, "timestamp": "2024-01-01T10:00:00Z"}
        ]
    }

@app.post("/predict", response_model=Prediction)
def predict(features: FeatureInput):
    # Ejemplo de predicción simulada para el portafolio
    return Prediction(prediction=0.72, confidence=0.85)
