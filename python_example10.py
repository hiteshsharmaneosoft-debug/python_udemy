## Example10: Currency Converter
# Convert USD to EUR & INR their will be two option for user to continue with 1 or 2 
# Multiply USD amount by exchange rate
# Practice working with floating-point numbers.


# Static exchange rates 
USD_TO_EUR = 0.92   # Example: 1 USD = 0.92 EUR
USD_TO_INR = 83.15  # Example: 1 USD = 83.15 INR

print("Currency Converter")
print("1. Convert USD to EUR")
print("2. Convert USD to INR")

choice = input("Enter your choice (1 or 2): ")

usd_amount = float(input("Enter amount in USD: $"))

if choice == "1":
    eur_amount = usd_amount * USD_TO_EUR
    print(f"${usd_amount:.2f} = €{eur_amount:.2f}")

elif choice == "2":
    inr_amount = usd_amount * USD_TO_INR
    print(f"${usd_amount:.2f} = ₹{inr_amount:.2f}")

else:
    print("Invalid choice! Please enter 1 or 2.")

