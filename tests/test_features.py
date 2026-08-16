import pandas as pd
import numpy as np
from src.utils.metrics import calculate_sharpe_ratio, calculate_max_drawdown

def test_calculate_sharpe_ratio():
    returns = pd.Series([0.01, -0.005, 0.02, -0.01])
    sharpe = calculate_sharpe_ratio(returns)
    assert isinstance(sharpe, float)

def test_calculate_max_drawdown():
    equity = pd.Series([100, 105, 95, 110])
    mdd = calculate_max_drawdown(equity)
    assert mdd < 0
    assert mdd == (95 - 105) / 105
