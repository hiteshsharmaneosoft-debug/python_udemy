## Example13: 
# Reverse a string with/without using slicing

x = "hitesh"
print("Original string:", x)

choice = input("Do you want to reverse the string using slicing? (yes/no): ").strip().lower()

if choice == "yes":
    # Using slicing
    reversed_string = x[::-1]
    print("Reversed string (using slicing):", reversed_string)
elif choice == "no":
    # Without using slicing
    reversed_string = ""
    for char in x:
        reversed_string = char + reversed_string
    print("Reversed string (without slicing):", reversed_string)
else:
    print("Invalid input! Please enter 'yes' or 'no'.")


# Find duplicates in a list

print("\nFind duplicates in a list")
from collections import Counter

input_list = [1, 7, 2, 3, 5, 7, 3, 3, 2, 1, 3]
print(input_list)

counts = Counter(input_list)
print(counts)

duplicates = [item for item, count in counts.items() if count > 1]
print(duplicates)



# Extract specific fields.

print("\nExtract specific fields")
person = "hitesh"
print(person)
print(person[-5])


# Write a function that checks if a number is prime : prime number is only divisible by 1 and itself.

print("\nNumber is Prime or Not")
def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # Check for factors from 2 to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, not prime

    return True  # No factors found, it's prime

num = int(input("Enter a number to check if it's prime: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
