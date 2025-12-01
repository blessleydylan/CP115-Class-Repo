position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here
if position == "Manager":
    base_rate = 30
elif position == "Supervisor":
    base_rate = 20  
elif position == "Staff":
    base_rate = 15
else:  # Intern
    base_rate = 8

if overtime_hours <= 8:
    overtime_pay = overtime_hours * base_rate * 1.5
else:
    overtime_pay = (8 * base_rate * 1.5) + ((overtime_hours - 8) * base_rate * 2.0)

if is_weekend == "Yes":
    overtime_pay += overtime_hours * 5  # RM5/hour weekend bonus


print(overtime_pay)