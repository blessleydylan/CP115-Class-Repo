# personal_data.py
# This script acts as a module to store and process personal information.
# It includes variable declarations, string operations, health calculations,
# and random element generation.

# Import the random and math modules
import random
import math

# --- Part 1: Personal Information Variables ---
full_name = "John Michael Doe"
age = 35
height_cm = 180
weight_kg = 82.5
phone_number = "555-0101"
email_address = "john.doe@email.com"
street_address = "123 Python Lane"
city = "Codeville"
postcode = "12345"

# --- Part 2: String Operations ---
# Full name in UPPERCASE and lowercase
full_name_upper = full_name.upper()
full_name_lower = full_name.lower()

# Length of the full name
name_length = len(full_name)

# Extract the first name and convert it to UPPERCASE
first_name = full_name.split()[0]
first_name_upper = first_name.upper()

# City name in UPPERCASE
city_upper = city.upper()

# Combine address parts into a full address string
full_address = f"{street_address}, {city}, {postcode}"

# Length of the full address
address_length = len(full_address)

# --- Part 3: Health Calculations ---
# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculate Body Mass Index (BMI)
# Formula: weight (kg) / (height (m))^2
bmi = weight_kg / (height_m ** 2)

# Calculate the square root of the BMI using the math module
bmi_sqrt = math.sqrt(bmi)

# --- Part 4: Random Elements ---
# Generate a random lucky number between 1 and 100
lucky_number = random.randint(1, 100)

# Choose a random color from a predefined list
colors = ["Red", "Green", "Blue"]
random_color = random.choice(colors)
