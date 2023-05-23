#Heart rate
#Author: josé Quemba

from datetime import datetime

current_date_and_time = datetime.now ()

day_of_week = 1#float(current_date_and_time.weekday ())

user_price = 1

# while loop and subtotaal calculation for the stretch part
while user_price != 0:
    print ()
    user_price = float(input('Please enter the price: '))
    user_quantity = float(input('Please enter the quantity: '))
    subtotal = float(user_price*user_quantity)
    print (f'The subtotal of your purchases is {subtotal:.2f}$')
    if subtotal >= 50 and day_of_week in (1,2):
        discount = subtotal*0.1
        sales_tax = (subtotal - discount)*0.06
        print (f'Discount amount: {discount:.2f}$')
        print (f'Sales tax amount: {sales_tax:.2f}$')
        print (f'Total: {subtotal - discount + sales_tax:.2f}$')
    elif subtotal > 0 < 50 or day_of_week in (0,3,4,5,6):
        sales_tax_no_discount = subtotal*0.06
        print (f'Sales tax amount: {sales_tax_no_discount:.2f}$')
        print (f'Total: {subtotal + sales_tax_no_discount:.2f}$')
else:
    if user_price == 0:
        print ('Thanks, goodbye...')

