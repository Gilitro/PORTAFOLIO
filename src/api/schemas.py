from pydantic import BaseModel, Field
from datetime import datetime

class MarketDataInput(BaseModel):
    """Schema para los datos de entrada hacia el modelo."""
    symbol: str = Field(..., description="Símbolo del activo (ej: EURUSD)")
    timestamp: datetime
    sma_20: float = Field(..., description="Media Móvil Simple de 20 periodos")
    rsi_14: float = Field(..., ge=0, le=100, description="Índice de Fuerza Relativa")
    macd: float
    atr_14: float = Field(..., gt=0)

class SignalResponse(BaseModel):
    """Schema para la respuesta de la API."""
    symbol: str
    timestamp: datetime
    action: str = Field(..., description="Acción sugerida: BUY, SELL, HOLD")
    confidence: float = Field(..., ge=0, le=1, description="Probabilidad o confianza del modelo")
    model_version: str
