## Example11 : Pizza Order verification system
# Receipt number validation, price calculation, User Input handeling, Error message
# TODO: 
    # get user input Slices, prices
    # Calculate total = slices * price
    # verify receipt -> if total == receipt print verified & else error


receipt_order = 2365 # 5×473 
slices = int(input("Enter the slices number: "))
price_per_slice = float(input("Enter the one slice price: ₹"))

total_bill = slices * price_per_slice
print(f"Total Bill amount is: ₹{total_bill:.2f}")

# print(receipt_order == total_bill)  # boolean expression result
if total_bill == receipt_order:
    print("Receipt Verified! Enjoy your Pizza ")
else:
    print("Error: Receipt mismatch. Please check again!")
