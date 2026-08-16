def test_dummy_backtest():
    # Simplemente validamos que el módulo exista y no contenga errores sintácticos
    try:
        from src.backtesting.backtest_example import run_dummy_backtest
        run_dummy_backtest()
        success = True
    except Exception as e:
        success = False
    
    assert success
