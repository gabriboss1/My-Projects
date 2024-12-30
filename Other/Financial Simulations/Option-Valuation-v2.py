import math
from scipy.stats import norm

def black_scholes(option_type, S0, K, T, r, sigma):
    try:
        d1 = (math.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        if option_type == "call":
            return S0 * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        elif option_type == "put":
            return K * math.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")
    except Exception as e:
        return f"Error in calculation: {e}"

def terminal_ui():
    print("Welcome to the Option Valuation Calculator (Black-Scholes Model)\n")
    print("Please provide the following parameters:")
    
    try:
        S0 = float(input("1. Stock Price (S₀): "))
        K = float(input("2. Strike Price (K): "))
        T = float(input("3. Time to Maturity (T, in years): "))
        r = float(input("4. Risk-Free Rate (r, as a decimal): "))
        sigma = float(input("5. Volatility (σ, as a decimal): "))
        
        option_type = input("6. Option Type (call or put): ").strip().lower()
        if option_type not in ["call", "put"]:
            print("Error: Invalid option type. Please enter 'call' or 'put'.")
            return
        
        price = black_scholes(option_type, S0, K, T, r, sigma)
        
        if isinstance(price, float):
            print(f"\nThe {option_type} option price is: {price:.2f}")
        else:
            print(f"\n{price}")
    except ValueError:
        print("\nError: Please enter valid numeric values for all inputs.")

if __name__ == "__main__":
    terminal_ui()
