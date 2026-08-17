import numpy as np

def calculate_sharpe_ratio(returns: np.ndarray, risk_free_rate: float = 0.0) -> float:
    """Calcula Sharpe Ratio"""
    excess_returns = returns - risk_free_rate
    if np.std(excess_returns) == 0:
        return 0
    return np.mean(excess_returns) / np.std(excess_returns)

def calculate_max_drawdown(equity_curve: np.ndarray) -> float:
    """Calcula máximo drawdown"""
    peak = np.maximum.accumulate(equity_curve)
    drawdown = (peak - equity_curve) / peak
    return np.max(drawdown)

def calculate_win_rate(trades: list) -> float:
    """Calcula win rate"""
    if not trades:
        return 0
    wins = sum(1 for t in trades if t['profit'] > 0)
    return wins / len(trades)
