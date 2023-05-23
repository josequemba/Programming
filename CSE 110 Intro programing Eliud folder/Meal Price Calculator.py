The_price_of_a_child_meal = float (input ("What is the price of a child's meal? "))
The_price_of_an_adult_meal = float (input ("What is the price of an adult's meal? "))
The_number_of_children = input ('How many children are there? ')
The_number_of_adult = input ('How many adults are there? ')
The_sales_tax_rate = float (input ('What is the sales tax rate? '))

Children_meal_price = float (The_price_of_a_child_meal) * float (The_number_of_children)
Adult_meal_price = float (The_price_of_an_adult_meal) * float (The_number_of_adult)
Tax_rate = float (The_sales_tax_rate) / 100
print ()

subtotal = float (Children_meal_price) + float (Adult_meal_price)
output= f'Subtotal: ${round (subtotal, 2)}'
print (output)

Tax = (float (Children_meal_price) + float (Adult_meal_price)) * Tax_rate
output = f'Sales Tax: ${round (Tax, 2)}'
print (output)
output = f'Total: ${round (subtotal + Tax, 2)}'
print (output)
print ()

Payment_amount = float (input ('What is the payment amount? '))
output = f'Change: ${round (float (Payment_amount) - (subtotal+Tax), 2)}'
print (output)
print ()
import datetime
now = datetime.datetime.now ()
print (now)