import yfinance as yf

spy = yf.download("SPY", start="2022-01-01", end="2026-04-29")

print(spy.head())



