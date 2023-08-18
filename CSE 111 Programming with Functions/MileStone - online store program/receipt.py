#Heart rate
#Author: josé Quemba
print ()

import csv
from datetime import datetime

def main ():

    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    try: 
        products_dict = read_dictionary ("C:\\Users\\Jose Eliud Dias\\Desktop\Programming\\CSE 111 Programming with Functions\\MileStone - online store program\\products.csv", PRODUCT_INDEX)

        #print(products_dict)
        print ()

        # printing the stores' name
        print ("Kero Nova Vida") 

         # opening the request file
        with open ("C:\\Users\\Jose Eliud Dias\\Desktop\Programming\\CSE 111 Programming with Functions\\MileStone - online store program\\request.csv", "rt") as products_data:
            reader = csv.reader (products_data)

            next (reader)

            print ()
            print ('Requested products: ')
            print ()

            sum_quantity = 0
            cost_subtotal = 0

            for data in reader:

                #separeting products requested and quantities
                product = data [0]
                quantity = data [1]

                #getting the requested product from the catalog (compound list)
                products = products_dict [product]

                #getting the name only
                products_name = products [NAME_INDEX]

                #getting the price only
                products_price = products [PRICE_INDEX]

                #printing the name, quantity and the price of each product requested
                print (f'{products_name}: Qt - {quantity}; price - ${products_price}')
           
                #computing all the values
                tax_rate = 6
                discount_rate = 10
                sum_quantity += int(quantity)
                cost_subtotal += float(products_price) * float(quantity)
                sales_tax = cost_subtotal * tax_rate / 100
                total_cost = cost_subtotal + sales_tax
                discount = total_cost * discount_rate / 100
                discount_total = total_cost - discount

    #Exceeding the Requirements --------------------------------------------------------
        #Get the week days in numer 
        current_date = datetime.now ()
        day_of_week = current_date.weekday ()

        #the week day in number
        #0 - Monday; 1 - Tuesday; 2 - Wednesday; 3 - Thursday; 4 - Friday; 5 - Saturday; 6 - Sunday.
        day_of_week_number = int(day_of_week)

        if day_of_week_number in (0,3,4,5,6):       
            #printing the sum of ordered items
            print ()
            print (f'Total of ordered items: {sum_quantity}')

            #printing the bubtotal of the ordered items
            print (f'Subtotal: {cost_subtotal:.2f}')

            #printing the sales tax amount
            print (f'Sales tax: {sales_tax:.2f}')

            #printing the total amount
            print (f'Total: {total_cost:.2f}')

            #message
            print()
            print ("Thanks for shopping at Kero Nova Vida Shopping.")

            #printing the current date and time
            current_date_and_time = datetime.now ()

            print (f'{current_date_and_time:%c}')
        else:
            print ()
            print (f'Total of ordered items: {sum_quantity}')

            #printing the bubtotal of the ordered items
            print (f'Subtotal: {cost_subtotal:.2f}')

            #printing the sales tax amount
            print (f'Sales tax: {sales_tax:.2f}')

            #printing the total amount
            print (f'Total without the discount: {total_cost:.2f}')

            #printing the discount
            print (f'Discount: {discount:.2f}')

            #printing the total amount
            print (f'Total with the discount: {discount_total:.2f}')

            #message
            print()
            print ("Thanks for shopping at Kero Nova Vida Shopping.")

            #printing the current date and time
            current_date_and_time = datetime.now ()

            print (f'{current_date_and_time:%c}')

        print()
    except FileNotFoundError as not_found_err:
        print (type(not_found_err).__name__, not_found_err, sep=": ")
        print ("A file is missing")

    except PermissionError as perm_err:
        print (type(perm_err).__name__, perm_err, sep=": ")
        print ("you have no permission to acess this file, please try another one.")

    except KeyError as key_err:
        print ("unknown product ID in the request.csv file", key_err)

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters"""
    products = {}

    with open (filename, "rt") as product_data:
        reader = csv.reader (product_data)

        next (reader)
        
        for data in reader:

            key = data [key_column_index]

            products [key] = data
    return products

if __name__ == "__main__":
    main ()
