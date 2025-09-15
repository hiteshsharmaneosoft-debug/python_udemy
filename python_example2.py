# Example2 : build smart bill spilliter

def smart_bill_splitter():
    print("Welcome to Smart Bill Splitter!")

    try:
        # Input total bill
        total_bill = float(input("Enter the total bill amount: ₹"))
        
        # Input number of people
        num_people = int(input("Enter the number of people splitting the bill: "))
        
        if num_people <= 0:
            print(" Number of people must be greater than 0.")
            return
        
        # Optional: tip
        add_tip = input("Do you want to add a tip? (yes/no): ").lower()
        tip_amount = 0.0
        if add_tip == "yes":
            tip_percentage = float(input("Enter tip percentage (e.g., 10 for 10%): "))
            tip_amount = (tip_percentage / 100) * total_bill
            total_bill += tip_amount

        # Split the bill
        split_amount = total_bill / num_people

        # Show results
        print("\nBill Summary:")
        print(f"Base Bill: ₹{total_bill - tip_amount:.2f}")
        print(f"Tip: ₹{tip_amount:.2f}")
        print(f"Total Bill (with tip): ₹{total_bill:.2f}")
        print(f"Each person should pay: ₹{split_amount:.2f}")

    except ValueError:
        print(" Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    smart_bill_splitter()
