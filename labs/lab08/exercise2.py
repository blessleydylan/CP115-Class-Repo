 # assign variables

no_friend = 6
no_main_dishes = 3
price_main_dishes = 25
no_appetizers = 2
price_appetizers = 12
no_drinks = 4
price_drinks = 8
delivery_fee = 5

 # calculation

total_bill_each = (((no_main_dishes * price_main_dishes + no_appetizers * price_appetizers + no_drinks * price_drinks) * 1.10) + 5 ) // 6

 # print output
print(total_bill_each)