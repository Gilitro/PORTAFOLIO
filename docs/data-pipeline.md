# Data Pipeline

El pipeline de procesamiento de datos se encarga de transformar datos en crudo en un dataset listo para el modelo.

## Etapas

1. **Extracción**: Obtención de precios (OHLCV).
2. **Limpieza**: Manejo de NaNs y detección de outliers.
3. **Generación de Features**:
   - Medias Móviles (SMA, EMA).
   - Indicadores de Volatilidad (Bollinger Bands, ATR).
   - Momentum (RSI, MACD).
4. **Normalización**: Escalamiento de las variables para los modelos.
