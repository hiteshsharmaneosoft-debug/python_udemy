# Example1: building a celsius to fahrenheit converter
def celsius_to_fahrenheit(celsius: float):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


if __name__ == "__main__":
    # Ask the user for input
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid number.")



