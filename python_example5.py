## Example5: fibonacci series
# Fibonacci series is a sequence where: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
# Each number = sum of the previous two numbers.


# Ask the user how many terms they want
n = int(input("Enter the number of terms for Fibonacci series: "))

# First two terms
a = 0
b = 1

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b   
