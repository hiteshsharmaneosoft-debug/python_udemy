## Example3: Movie Theater Seating
# We have: Total seats = 52
# Friends group = 7 (they must sit together in the same row)
# We want to calculate:
    # How many complete rows we can fill.
    # How many seats will be left over in the partially filled row.
    # graphical representation of the output

total_seats = 58
group_size = 6

# Full rows of friends that can be seated : Floor Division
full_rows = total_seats // group_size

# Seats left that can't complete a row : Modulus Operator
left_over_seats = total_seats % group_size

print("Number of full rows that can be fill:", full_rows)
print("left over seats in the rows:", left_over_seats)

# graphical representation
print("\nSeating Arrangement:\n")

# Draw full rows
for row in range(full_rows):
    print("Row", row + 1, ":", "F " * group_size)

# Draw last row if any seats left
if left_over_seats > 0:
    print("Row", full_rows + 1, ":", "F " * left_over_seats + "_ " * (group_size - left_over_seats))
