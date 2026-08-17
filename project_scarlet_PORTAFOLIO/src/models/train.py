from catboost import CatBoostClassifier
import pandas as pd

def train_example_model(X_train: pd.DataFrame, y_train: pd.Series):
    """Entrena modelo de ejemplo con datos sintéticos"""
    model = CatBoostClassifier(
        iterations=100,
        depth=6,
        learning_rate=0.1,
        verbose=False
    )
    model.fit(X_train, y_train)
    return model

def predict_example(model, X: pd.DataFrame) -> pd.Series:
    """Genera predicciones de ejemplo"""
    return model.predict(X)
