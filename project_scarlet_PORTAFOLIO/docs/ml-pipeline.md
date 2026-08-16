# ML Pipeline

La estrategia predictiva se basa en un modelo **CatBoost** optimizado para datos tabulares y series de tiempo con features categóricos y numéricos.

## Flujo de Entrenamiento

1. **Split de Datos**: Separación cronológica en Train, Validation y Test (Walk-forward cross-validation).
2. **Feature Selection**: Selección de las variables con mayor importancia basada en SHAP values.
3. **Entrenamiento**: Ajuste del modelo CatBoost (Classification o Regression dependiendo de la señal).
4. **Evaluación**: Monitoreo en el conjunto de validación para evitar overfitting.
