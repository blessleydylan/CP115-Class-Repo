# --- Item Cost Calculator ---

# Get the item name and price from the user
# Note: input() returns a string, so we need to convert the price to a float
item_name = input("Enter the item name: ")
item_price_str = input(f"Enter the price for one {item_name}: ")

# Use a try-except block to handle potential errors if the user enters non-numeric input for the price
try:
    item_price = float(item_price_str)
except ValueError:
    print("Invalid price entered. Please enter a number.")
    # Exit the program if the price is not a valid number
    exit()

# Define the program's variables
quantity = 3
tax_rate = 0.06  # 6% tax rate

# Perform the calculations
subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

# Display the results to the user
print("\n--- Receipt ---")
print(f"Item:          {item_name}")
print(f"Quantity:      {quantity}")
print("-" * 25)
print(f"Subtotal:      ${subtotal:,.2f}")
print(f"Tax ({tax_rate * 100:.0f}%):    ${tax_amount:,.2f}")
print(f"Total Cost:    ${total_cost:,.2f}")
print("-" * 25)
