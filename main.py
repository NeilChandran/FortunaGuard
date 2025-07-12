"""
FortunaGuard Main Entry Point
Handles CLI and orchestrator invocation.
"""

from orchestrator import Orchestrator

def main_menu():
    print("\nWelcome to FortunaGuard: Wealth & Risk Analytics Suite")
    print("1. Analyze Portfolio")
    print("2. Run Risk Analysis")
    print("3. Simulate Portfolio")
    print("4. Generate Report")
    print("5. Exit")

def main():
    orchestrator = Orchestrator()
    while True:
        main_menu()
        choice = input("Select an option: ")
        if choice == "1":
            orchestrator.analyze_portfolio()
        elif choice == "2":
            orchestrator.analyze_risk()
        elif choice == "3":
            orchestrator.run_simulation()
        elif choice == "4":
            orchestrator.generate_report()
        elif choice == "5":
            print("Exiting FortunaGuard. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

