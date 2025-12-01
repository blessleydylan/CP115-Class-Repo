employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()
net_salary = 0

if tax_status == "Single":
    if base_salary >= 5000:
        tax_rate = 0.22
    else:   
        tax_rate = 0.18
elif tax_status == "Married":
    if base_salary >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status == "Head":
    if base_salary >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19

overtime_pay = overtime_hours * 35
net_salary = (base_salary + overtime_pay) * (1 - tax_rate) * 0.885

tax_rate = int(tax_rate * 100)

print(employee_name)
print(tax_rate, end="%\n")
print(f"{net_salary:.2f}")