#Shopping cart along with their prices
#Author: josé Quemba
print ()
print ('Welcome to the Shopping Cart Program!')
print ()
options = ['0', 'Add item', 'View cart', 'Remove item', 'Compute total', 'Quit']
items = []
select_action = 0

while select_action != 5:
    print ('Please select one of the following:')
    for i in range (1, 6):
        word = options [i]
        print (f'{i}. {word}')
    select_action = int(input ('Please enter an action: '))
    if select_action == 1:
        item = input ('What item would you like to add? ')
        items.append (item)
        print (f'"{item}"has been added to the cart.')
        print ()
    elif select_action == 2:
        for words in items:
            print (words)
    print ()
else:
    print ('Thank you. Goodbye.')