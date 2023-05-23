#Shopping cart along with their prices
#Author: josé Quemba
print ()

items = []
user = 'Alma'

print ('Please enter the items of the shopping list (type: quit to finish):')
while user != 'Quit':
    user = input ('Item: ').capitalize ()
    if user != 'Quit':
        items.append (user)

print ()
print ('The shopping list is:')
for word in items:
    print (word)

print ()
print ('The shopping list with indexes is:')
for i in range (len(items)):
    w = items [i]
    print (f'{i}. {w}')

print ()
change = int(input ('Which item would you like to change? '))
new_Item = input ('What is the new item? ')
print ()

print ('The shopping list with indexes is:')
items [change] = new_Item

for i in range (len(items)):
    wo = items [i]
    print (f'{i}. {wo}')