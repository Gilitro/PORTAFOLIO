import pandas as pd
import numpy as np

def run_dummy_backtest():
    """
    Simulación muy simplificada de un backtest.
    Genera un PnL ficticio y calcula métricas básicas.
    """
    print("Iniciando simulación de backtest...")
    
    # Generar rendimientos diarios simulados
    np.random.seed(123)
    days = 252 # ~1 año de trading
    
    # Media ligeramente positiva y volatilidad realista
    daily_returns = np.random.normal(0.0005, 0.01, days)
    
    # Vector de precios acumulado (base 100)
    equity_curve = 100 * np.exp(np.cumsum(daily_returns))
    
    # Cálculo de rendimiento total
    total_return = (equity_curve[-1] / equity_curve[0]) - 1
    
    # Cálculo Sharpe Ratio simplificado (Asumiendo Risk-Free = 0)
    sharpe_ratio = np.sqrt(252) * (np.mean(daily_returns) / np.std(daily_returns))
    
    print(f"Backtest Completado.")
    print(f"Rendimiento Total: {total_return:.2%}")
    print(f"Sharpe Ratio Anualizado: {sharpe_ratio:.2f}")

if __name__ == "__main__":
    run_dummy_backtest()
