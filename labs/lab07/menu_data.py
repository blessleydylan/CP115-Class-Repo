 # Import random module
import random

# Set Variables for menu_data
restaurant_name = "Aieman Cafe"
restaurant_location = "Hati Aieman"
tax_rate = 0.06
service_charge = 0.1
item1 = "Chicken"
item1_price = 5 + (5 * tax_rate) + (5 * service_charge)
item2 = "Dog"
item2_price = 6 + (6 * tax_rate) + (6 * service_charge)
item3 = "Cat"
item3_price = 7 + (7 * tax_rate) + (7 * service_charge)

restaurantupper = restaurant_name.upper()
restaurantlower = restaurant_name.lower()
restaurant_length = len(restaurant_name)

special_number = random.randint(1, 3)
customer_number = random.randint(100, 999)
