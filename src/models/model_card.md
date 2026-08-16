# Model Card - Project Scarlet

## Información General
- **Algoritmo**: CatBoost Classifier
- **Versión**: 1.0.0
- **Tarea**: Clasificación binaria (Señal de entrada direccional)

## Detalles de Entrenamiento
- **Optimizador**: Gradiente descendente estocástico (optimizado por CatBoost)
- **Loss Function**: Logloss
- **Métricas Primarias**: Accuracy, Precision, F1-Score

## Features Utilizados
- Medias Móviles (SMA 20, 50, 200)
- RSI (14, 21 periodos)
- MACD y Señal
- Average True Range (ATR)

## Limitaciones Generales
- Rendimiento dependiente de la liquidez del mercado.
- Sensible a eventos macroeconómicos no capturados en series de precios.

*(Nota: Los pesos reales y la estrategia de parámetros óptima se mantienen privados para preservar la ventaja del sistema).*
