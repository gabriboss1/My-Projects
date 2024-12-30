import numpy as np
from tqdm import tqdm

def monte_carlo_option_pricing(S0, K, T, r, sigma, num_simulations, option_type="call"):

    payoffs = []
    for _ in tqdm(range(num_simulations), desc="Simulating paths", unit="simulation"):
        Z = np.random.standard_normal()
        ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

        if option_type == "call":
            payoff = max(ST - K, 0)
        elif option_type == "put":
            payoff = max(K - ST, 0)
        else:
            raise ValueError("Invalid option type. Choose 'call' or 'put'.")

        payoffs.append(payoff)

    option_price = np.exp(-r * T) * np.mean(payoffs)

    return option_price

if __name__ == "__main__":
    print("=" * 50)
    print("\tMonte Carlo Option Pricing Tool")
    print("=" * 50)
    print("Please provide the following parameters:\n")

    try:
        S0 = float(input("Initial stock price (S0): "))
        K = float(input("Strike price (K): "))
        T = float(input("Time to maturity in years (T): "))
        r = float(input("Risk-free interest rate (r) in decimal (e.g., 0.05 for 5%): "))
        sigma = float(input("Volatility (sigma) in decimal (e.g., 0.2 for 20%): "))
        num_simulations = int(input("Number of Monte Carlo simulations: "))
        option_type = input("Option type (call/put): ").strip().lower()

        if option_type not in ["call", "put"]:
            print("Invalid option type. Please restart and choose 'call' or 'put'.")
        else:
            print("\nCalculating, please wait...\n")
            option_price = monte_carlo_option_pricing(S0, K, T, r, sigma, num_simulations, option_type)
            print(f"\nEstimated {option_type.capitalize()} Option Price: {option_price:.2f}")
    except ValueError:
        print("Invalid input. Please restart and enter valid values.")

    print("\nThank you for using the Monte Carlo Option Pricing Tool!")
