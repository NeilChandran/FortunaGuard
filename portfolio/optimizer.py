"""
PortfolioOptimizer: Optimizes portfolio allocation for maximum Sharpe ratio.
"""

import numpy as np
from scipy.optimize import minimize

class PortfolioOptimizer:
    def optimize(self, returns, initial_weights):
        n_assets = returns.shape[1]
        mean_returns = returns.mean() * 252
        cov_matrix = returns.cov() * 252

        def neg_sharpe(weights):
            port_return = np.dot(weights, mean_returns)
            port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            return -port_return / port_vol

        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(n_assets))
        result = minimize(neg_sharpe, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        print(f"Optimized weights: {result.x}")
        return result.x

    def performance(self, returns, weights):
        mean_returns = returns.mean() * 252
        cov_matrix = returns.cov() * 252
        port_return = np.dot(weights, mean_returns)
        port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        sharpe = port_return / port_vol
        return {'return': port_return, 'volatility': port_vol, 'sharpe': sharpe}
