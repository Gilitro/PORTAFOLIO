import pandas as pd
import numpy as np

def calculate_moving_average(df: pd.DataFrame, window: int = 20) -> pd.Series:
    """Calcula media móvil simple"""
    return df['close'].rolling(window=window).mean()

def calculate_volatility(df: pd.DataFrame, window: int = 20) -> pd.Series:
    """Calcula volatilidad (desviación estándar)"""
    return df['close'].rolling(window=window).std()

def calculate_rsi(df: pd.DataFrame, window: int = 14) -> pd.Series:
    """Calcula RSI (ejemplo educativo)"""
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
