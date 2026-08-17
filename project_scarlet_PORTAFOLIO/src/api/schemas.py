from pydantic import BaseModel

class Signal(BaseModel):
    id: int
    symbol: str
    direction: str
    probability: float
    timestamp: str

class FeatureInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    # Más features genéricos...

class Prediction(BaseModel):
    prediction: float
    confidence: float
