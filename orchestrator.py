"""
Orchestrator: Coordinates all modules in FortunaGuard.
"""

from data.fetcher import DataFetcher
from data.cleaner import DataCleaner
from data.processor import DataProcessor
from portfolio.allocator import PortfolioAllocator
from portfolio.optimizer import PortfolioOptimizer
from portfolio.simulator import PortfolioSimulator
from risk.metrics import RiskMetrics
from risk.stress_test import StressTest
from visualization.charts import ChartVisualizer
from visualization.report import ReportGenerator

class Orchestrator:
    def __init__(self):
        self.tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
        self.start_date = "2020-01-01"
        self.end_date = "2023-01-01"
        self.data_fetcher = DataFetcher(self.tickers, self.start_date, self.end_date)
        self.data_cleaner = DataCleaner()
        self.data_processor = DataProcessor()
        self.allocator = PortfolioAllocator()
        self.optimizer = PortfolioOptimizer()
        self.simulator = PortfolioSimulator()
        self.risk_metrics = RiskMetrics()
        self.stress_test = StressTest()
        self.visualizer = ChartVisualizer()
        self.reporter = ReportGenerator()
        self.data = None
        self.cleaned_data = None
        self.returns = None
        self.weights = None
        self.optimized_weights = None
        self.simulation_results = None
        self.risks = None
        self.stress_results = None

    def analyze_portfolio(self):
        print("\n[Portfolio Analysis]")
        self.data = self.data_fetcher.fetch()
        self.cleaned_data = self.data_cleaner.clean(self.data)
        self.returns = self.data_processor.process(self.cleaned_data)
        self.weights = self.allocator.allocate(self.returns)
        self.optimized_weights = self.optimizer.optimize(self.returns, self.weights)
        print("[INFO] Portfolio weights:", self.optimized_weights)
        perf = self.optimizer.performance(self.returns, self.optimized_weights)
        print(f"Expected Annual Return: {perf['return']:.2%}")
        print(f"Annual Volatility: {perf['volatility']:.2%}")
        print(f"Sharpe Ratio: {perf['sharpe']:.2f}")

    def analyze_risk(self):
        print("\n[Risk Analysis]")
        if self.returns is None or self.optimized_weights is None:
            print("Please run Portfolio Analysis first.")
            return
        self.risks = self.risk_metrics.calculate(self.returns, self.optimized_weights)
        for k, v in self.risks.items():
            print(f"{k}: {v:.4f}")

    def run_simulation(self):
        print("\n[Portfolio Simulation]")
        if self.returns is None or self.optimized_weights is None:
            print("Please run Portfolio Analysis first.")
            return
        self.simulation_results = self.simulator.simulate(self.returns, self.optimized_weights)
        print(f"Simulated {len(self.simulation_results)} portfolio returns.")

    def generate_report(self):
        print("\n[Generating Report]")
        if self.simulation_results is None or self.risks is None:
            print("Please run Portfolio and Risk Analysis first.")
            return
        self.stress_results = self.stress_test.run(self.returns, self.optimized_weights)
        self.visualizer.plot(self.simulation_results, self.risks)
        self.reporter.generate(self.simulation_results, self.risks, self.stress_results)
        print("Report generated: report.txt")
