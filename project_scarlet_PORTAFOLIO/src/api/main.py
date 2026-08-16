from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
from typing import Dict, Any

from .schemas import MarketDataInput, SignalResponse

app = FastAPI(
    title="Project Scarlet API",
    description="API de señales de trading algorítmico",
    version="1.0.0"
)

@app.get("/health")
def health_check() -> Dict[str, str]:
    """Verifica el estado de la API."""
    return {"status": "ok", "service": "Project Scarlet API"}

@app.post("/predict", response_model=SignalResponse)
def get_prediction(data: MarketDataInput) -> SignalResponse:
    """
    Recibe un vector de features y devuelve la predicción del modelo.
    (Ejemplo simulado)
    """
    if data.rsi_14 < 10 or data.rsi_14 > 90:
        raise HTTPException(status_code=400, detail="Valores de RSI fuera de rango lógico")
    
    # Lógica mockeada: simulando inferencia del modelo
    prob = random.uniform(0, 1)
    action = "BUY" if prob > 0.6 else "SELL" if prob < 0.4 else "HOLD"
    
    return SignalResponse(
        symbol=data.symbol,
        timestamp=data.timestamp,
        action=action,
        confidence=prob,
        model_version="v1.0-sim"
    )
