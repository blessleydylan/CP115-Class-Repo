age = int(input())
tickets_sold = 0
total_revenue = 0

# TODO: Your code here
while age != -1:
    if age <= 12:
        price = 8
    elif 13 <= age <= 17:
        price = 10
    elif 18 <= age <= 64:
        price = 15
    else:  # age >= 65
        price = 10

    tickets_sold += 1
    total_revenue += price

    age = int(input())
print(tickets_sold)
print(total_revenue)
