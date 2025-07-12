"""
DataCleaner: Cleans and preprocesses raw price data.
"""

import pandas as pd

class DataCleaner:
    def clean(self, data):
        if data.empty:
            print("No data to clean.")
            return data
        data = data.fillna(method='ffill').dropna()
        if data.isnull().values.any():
            print("[Warning] Null values remain after cleaning.")
        return data
