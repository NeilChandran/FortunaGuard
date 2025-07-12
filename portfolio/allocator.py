"""
PortfolioAllocator: Allocates weights to assets.
"""

import numpy as np

class PortfolioAllocator:
    def allocate(self, returns):
        n_assets = returns.shape[1]
        weights = np.ones(n_assets) / n_assets
        print(f"Equal-weighted allocation: {weights}")
        return weights
