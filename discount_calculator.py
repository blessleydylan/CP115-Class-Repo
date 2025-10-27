# Input values for Age and TicketPrice

Age = int(input("Enter your age(Integer): "))
TicketPrice = float(input("Enter the ticket price(Float): "))

# Check for invalid inputs

if TicketPrice < 0:
    print("Invalid Ticket Price Value!")

elif Age < 0:
    print("Invalid Age Value!")

# Determine discount based on age

else:
    if Age <= 12:
        DiscountCategory = "Children(50% Discount)"
        Discount = 0.50

    elif Age <= 17:
         DiscountCategory = "Teenagers(25% Discount)"
         Discount = 0.25

    else:
         DiscountCategory = "Adults(No Discount)"
         Discount = 0

# Calculate discounted price and print results
    DiscountedPrice = TicketPrice * (1 - Discount)
    print("Discount Category:", DiscountCategory)
    print("Discounted Price: RM", DiscountedPrice)