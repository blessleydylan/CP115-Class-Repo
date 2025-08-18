 # Import menu_data.py
import menu_data

 # Print message using f-string
 #import school_data.py
import school_data

print(f"Welcome to {menu_data.restaurant_name}")
print(f"Customer Number: {menu_data.customer_number}")
print(f"---Menu---")
print(f"{menu_data.item1}: {menu_data.item1_price}")
print(f"{menu_data.item2}: {menu_data.item2_price}")
print(f"{menu_data.item3}: {menu_data.item3_price}")
print(f"Today's Special Menu: {menu_data.special_number}")
