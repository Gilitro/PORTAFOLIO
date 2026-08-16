# Project Scarlet - Portfolio

Sistema de trading algorítmico desarrollado en Python que integra análisis de mercado, machine learning (CatBoost) y ejecución controlada.

## ⚠️ Nota

Este repositorio contiene una versión educativa y simplificada del sistema. No incluye la estrategia completa ni datos reales de operación.

## Arquitectura

El flujo de procesamiento es el siguiente:
1. **Datos**: Ingesta de datos de mercado históricos.
2. **Features**: Generación de variables técnicas y estadísticas.
3. **Modelo**: Entrenamiento y validación de CatBoost.
4. **Señales**: Generación de predicciones y señales de trading.
5. **Ejecución**: Simulación controlada de operaciones.

## Tecnologías

- Python 3.11+
- FastAPI
- PostgreSQL
- CatBoost
- Docker
- pytest

## Estructura

- `src/data/`: Pipeline de datos y features
- `src/models/`: Entrenamiento y validación
- `src/api/`: API REST para señales
- `src/backtesting/`: Backtesting con datos sintéticos
- `tests/`: Pruebas unitarias y de integración

## Ejecución local

```bash
docker-compose up --build
```

## API

Endpoints disponibles en `/docs` (Swagger UI).

## Métricas de ejemplo

- Sharpe Ratio (datos sintéticos): 1.85
- Win Rate simulado: 56.4%
- Máximo drawdown: 8.2%

## Pruebas

```bash
pytest
```

## Autor

Alan Gilberto Guzmán Viniegra
[LinkedIn] | [Portfolio]
