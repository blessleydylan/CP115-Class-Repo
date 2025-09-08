day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# TODO your code here
if day_type == "Weekends":
    if show_time > 17:
        if customer_type == "Child":
            base_price = 15
        elif customer_type == "Adult":
            base_price = 21
        else:  # Senior
            base_price = 15
    else:
        if customer_type == "Child":
            base_price = 12
        elif customer_type == "Adult":
            base_price = 18
        else:  # Senior
            base_price = 12
else:  # Weekdays
    if show_time > 17:
        if customer_type == "Child":
            base_price = 13
        elif customer_type == "Adult":
            base_price = 18
        else:  # Senior
            base_price = 15
    else:
        if customer_type == "Child":
            base_price = 10
        elif customer_type == "Adult":
            base_price = 15
        else:  # Senior
            base_price = 12

if is_student == "Yes":
    final_price = base_price * 0.9

print(base_price)
print(final_price)