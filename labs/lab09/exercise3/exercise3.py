day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# TODO your code here
if day_type == "Weekend":
    if show_time > 18:
        if customer_type == "Child":
            base_price = 12
        elif customer_type == "Adult":
            base_price = 18
        else:  # Senior
            base_price = 15
    else:
        if customer_type == "Child":
            base_price = 12
        elif customer_type == "Adult":
            base_price = 18
        else:  # Senior
            base_price = 15
else:  # Weekdays
    if show_time > 18:
        if customer_type == "Child":
            base_price = 10
        elif customer_type == "Adult":
            base_price = 15
        else:  # Senior
            base_price = 12
    else:
        if customer_type == "Child":
            base_price = 10
        elif customer_type == "Adult":
            base_price = 15
        else:  # Senior
            base_price = 12

if show_time > 18:
    final_price = base_price + 3
else:
    final_price = base_price

if is_student == "Yes" and day_type == "Weekday":
    final_price = final_price * 0.9


print(int(base_price))
print(float(final_price))