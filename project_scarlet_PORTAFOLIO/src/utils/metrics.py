import numpy as np
import pandas as pd

def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0, periods: int = 252) -> float:
    """Calcula el Sharpe Ratio anualizado."""
    if len(returns) == 0:
        return 0.0
    excess_returns = returns - risk_free_rate
    mean_return = excess_returns.mean()
    std_return = excess_returns.std()
    
    if std_return == 0:
        return 0.0
    
    return np.sqrt(periods) * (mean_return / std_return)

def calculate_max_drawdown(equity_curve: pd.Series) -> float:
    """Calcula el Maximum Drawdown histórico."""
    if len(equity_curve) == 0:
        return 0.0
    rolling_max = equity_curve.cummax()
    drawdowns = (equity_curve - rolling_max) / rolling_max
    return drawdowns.min()
