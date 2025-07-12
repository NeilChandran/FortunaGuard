"""
ReportGenerator: Generates a summary report.
"""

class ReportGenerator:
    def generate(self, simulation_results, risks, stress_results):
        with open("report.txt", "w") as f:
            f.write("=== Portfolio Simulation Results ===\n")
            f.write(f"Mean Simulated Return: {sum(simulation_results)/len(simulation_results):.4f}\n")
            f.write("=== Risk Metrics ===\n")
            for k, v in risks.items():
                f.write(f"{k}: {v}\n")
            f.write("=== Stress Test Results ===\n")
            for k, v in stress_results.items():
                f.write(f"{k}: {v}\n")
            f.write("\nSee simulation_histogram.png for return distribution.\n")
