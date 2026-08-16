import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_dummy_model():
    """
    Ejemplo representativo del entrenamiento del modelo usando CatBoost.
    Utiliza datos sintéticos para demostración.
    """
    # 1. Generar datos sintéticos
    np.random.seed(42)
    n_samples = 1000
    
    X = pd.DataFrame({
        'sma_20': np.random.normal(1.05, 0.01, n_samples),
        'rsi_14': np.random.uniform(30, 70, n_samples),
        'macd': np.random.normal(0, 0.002, n_samples),
        'atr_14': np.random.uniform(0.001, 0.005, n_samples)
    })
    
    # Target binario (1: Comprar, 0: No operar/Vender)
    y = np.where(X['rsi_14'] < 40, 1, np.where(X['rsi_14'] > 60, 0, np.random.choice([0, 1], n_samples)))
    
    # 2. Split de datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # 3. Entrenamiento con CatBoost
    model = CatBoostClassifier(
        iterations=100,
        learning_rate=0.05,
        depth=6,
        eval_metric='Accuracy',
        random_seed=42,
        verbose=10
    )
    
    model.fit(
        X_train, y_train,
        eval_set=(X_test, y_test),
        early_stopping_rounds=20
    )
    
    # 4. Evaluación simple
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"\\nModelo entrenado con precisión de: {acc:.4f}")
    
    return model

if __name__ == "__main__":
    train_dummy_model()
