#Shopping cart along with their prices
#Author: josé Quemba
print ()
print ('Welcome to the Shopping Cart Program!')
print ()
options = ['0', 'Add item', 'View cart', 'Remove item', 'Compute total', 'Quit']
items = ['']
prices = [0]
select_action = 0
while select_action != 5:
    # Displaying the actions
    print ('Please select one of the following:')
    for i in range (1, 6):
        word = options [i]
        print (f'{i}. {word}')
    select_action = int(input ('Please enter an action: '))
    # Action 1 - storing the names and the prices
    if select_action == 1:
        item = input ('What item would you like to add? ')
        items.append (item)
        price = int(input(f'What is the price o the {item}? '))
        prices.append (price)
        print (f'"{item}"has been added to the cart.')
        print ()
    # Action 2 - Displaying the items with prices and index starting with 1...
    elif select_action == 2:   
        for i in range (1, len(items)):
            thing = items [i]
            amount = prices [i]
            print (f'{i}. {thing} - ${amount :.2f}')
    # Action 3 removing an item
    elif select_action == 3:
        item_for_removal = int(input ('Which item would you like to remove? '))
        items.pop (item_for_removal)
        prices.pop (item_for_removal)
        print ('Item removed.')
    # Action 4 computing the total
    elif select_action == 4:
        price_total= sum(prices)
        print (f'The total price of the items in the shopping cart is ${price_total :.2f}')
    print ()
else:
    print ('Thank you. Goodbye.')