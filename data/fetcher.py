"""
DataFetcher: Downloads historical price data using yfinance.
"""

import yfinance as yf
import pandas as pd

class DataFetcher:
    def __init__(self, tickers, start, end):
        self.tickers = tickers
        self.start = start
        self.end = end

    def fetch(self):
        try:
            print(f"Fetching data for: {', '.join(self.tickers)}")
            data = yf.download(self.tickers, start=self.start, end=self.end)["Adj Close"]
            if isinstance(data, pd.Series):
                data = data.to_frame()
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
