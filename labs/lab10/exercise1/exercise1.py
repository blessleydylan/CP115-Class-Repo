position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25    
else:
    hourly_rate = 18

overtime_pay = (overtime_hours * hourly_rate * 1.5) + (overtime_hours * 6 if is_weekend == "Yes" else 0)
total_pay = overtime_pay




print(hourly_rate)
print(overtime_pay)
print(total_pay)