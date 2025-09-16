## Example8: star pattern structure


# Ask the user for number of rows
rows = int(input("Enter the number of rows: "))

# Loop through rows
for i in range(1, rows + 1):
    # Print spaces (for alignment)
    print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))
