"""
PortfolioSimulator: Monte Carlo simulation of portfolio returns.
"""

import numpy as np

class PortfolioSimulator:
    def simulate(self, returns, weights, n_simulations=1000):
        simulation_results = []
        port_returns = returns @ weights
        for _ in range(n_simulations):
            simulated = np.random.choice(port_returns, size=len(port_returns), replace=True)
            simulation_results.append(np.sum(simulated))
        return simulation_results
