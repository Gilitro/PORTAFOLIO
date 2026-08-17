import pandas as pd
import numpy as np

def generate_sample_data(n_rows: int = 1000):
    """Genera datos sintéticos para ejemplo"""
    np.random.seed(42)
    
    dates = pd.date_range(start='2024-01-01', periods=n_rows, freq='h')
    close = 1.1 + np.cumsum(np.random.randn(n_rows) * 0.001)
    
    df = pd.DataFrame({
        'timestamp': dates,
        'open': close + np.random.randn(n_rows) * 0.0005,
        'high': close + np.abs(np.random.randn(n_rows) * 0.001),
        'low': close - np.abs(np.random.randn(n_rows) * 0.001),
        'close': close,
        'volume': np.random.randint(500, 2000, n_rows)
    })
    
    return df
