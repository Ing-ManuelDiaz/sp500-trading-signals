import yfinance as yf
import pandas as pd

def download_data(ticker="^GSPC", start="2020-01-01", end=None):
    """
    Download historical data for a given ticker.
    Default is S&P 500 index.
    """
    data = yf.download(ticker, start=start, end=end)
    return data

if __name__ == "__main__":
    df = download_data()
    print(df.head())
