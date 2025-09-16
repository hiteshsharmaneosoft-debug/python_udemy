## Example7: Some Arithmatic expression
    # Parenthesis()
    # Exponentiation **
    # Multiplication *, Division /, Integer Division //, Modulo %
    # Addition +, Subtraction -


result1 = (2 + 3) * 4     # Parentheses first → (5) * 4 = 20
print(result1)

result2 = (10 - 3) * (2 + 2)  # (7) * (4) = 28
print(result2)


result3 = 2 ** 3 * 2     # Exponent first → (8 * 2) = 16
print(result3)

result4 = (3 + 1) ** 2   # Parentheses first, then exponent → (4) ** 2 = 16
print(result4)

result5 = 100 - (50 + 25)  # Parentheses first → 100 - 75 = 25
print(result5)

result6 = (3 ** 4) % 5
print(result6)


print(52 // 7)
print(52 % 7)
