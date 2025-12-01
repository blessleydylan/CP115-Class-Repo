main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here
if main_course == "Chicken":    
    main_course_price = 10.0
elif main_course == "Beef":   
    main_course_price = 12.0
elif main_course == "Fish":    
    main_course_price = 11.0

if drink == "Soft Drink":    
    drink_price = 2.0
elif drink == "Coffee":    
    drink_price = 3.0

if dessert == "Ice Cream":    
    dessert_price = 4.0 
elif dessert == "Cake":
    dessert_price = 5.0

base_bill = main_course_price + drink_price + dessert_price
service_charge = base_bill * 0.10
total_bill = base_bill + service_charge

if customer_age >= 60:
    final_bill = total_bill * 0.85  # 15% discount for seniors
elif customer_age <= 18:
    final_bill = total_bill * 0.90  # 10% discount for students
else:
    final_bill = total_bill  # No discount

print(f"{final_bill:.2f}")