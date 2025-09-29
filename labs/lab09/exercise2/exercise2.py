employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

extra_payment = overtime_hours * 35
# This is the gross salary before taxes
gross_salary = base_salary + extra_payment

# A flag to track if we found a valid tax status
is_status_valid = True

# Determine the tax rate using nested conditions for better readability
if tax_status == 'Single':
    if base_salary >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == 'married':
    if base_salary >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status == 'Head':
    if base_salary >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19
else:
    # If the status isn't valid, print an error and set the flag to false
    is_status_valid = False
    print("Invalid tax status")

# Only perform the final calculation and print if the tax status was valid
# This prevents the program from crashing
if is_status_valid:
    net_salary = gross_salary * (1 - tax_rate)
    
    print(employee_name)
    print(tax_rate)
    print(f"{net_salary:.2f}")