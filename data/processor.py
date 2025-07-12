"""
DataProcessor: Processes cleaned data to calculate returns and features.
"""

import pandas as pd

class DataProcessor:
    def process(self, data):
        if data.empty:
            print("No data to process.")
            return pd.DataFrame()
        returns = data.pct_change().dropna()
        # Add more features if needed
        returns['Portfolio'] = returns.mean(axis=1)
        return returns

