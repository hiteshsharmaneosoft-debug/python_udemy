## Example6: With the use of input() & import module create a Age calculator
# Pass a current year and ask user to put their birth year
# write a python script to find user's age


from datetime import datetime

# current_year = 2025
current_year = datetime.now().year
birth_year = input("Enter your birth year:")
birth_year = int(birth_year)

# Validation: birth year should not be greater than current year
if birth_year > current_year:
    print("Error: Birth year cannot be in the future. Please enter a valid year.")
else:
    age = current_year - birth_year
    print(f"You are {age} years old.")

