# Architecture

```mermaid
graph TD
    A[Market Data Source] -->|Ingestion| B[Data Pipeline]
    B -->|Cleaning & Transformation| C[Feature Engineering]
    C -->|Feature Store| D[Machine Learning Model - CatBoost]
    D -->|Predictions| E[Signal Generator]
    E -->|Trading Signals| F[API / Execution Engine]
    
    F -->|Orders| G[Broker Simulation]
    G -->|Execution Feedback| F
```

## Componentes Principales

1. **Data Pipeline**: Limpia y estructura los datos.
2. **Feature Engineering**: Crea indicadores técnicos.
3. **ML Model**: Genera predicciones basadas en datos históricos (CatBoost).
4. **Execution Engine (API)**: Recibe señales y expone la API.
