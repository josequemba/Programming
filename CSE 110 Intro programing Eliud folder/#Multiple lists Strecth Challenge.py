#Multiple lists Strecth Challenge
#Shopping cart along with their prices
#Author: josé Quemba
print ()
accounts = []
balances = []

print ('Enter the names and balances of bank accounts (type: quit when done)')
user_account = 'Alma'

while user_account != 'Quit':
    user_account = input ('What is the name of this account? ').capitalize ()
    if user_account != 'Quit':
        accounts.append (user_account)
    if user_account != 'Quit':
        user_balance = int(input ('What is the balance? '))
        balances.append (user_balance)
print ()

print ('Account Information:')
for i in range (len(accounts)):
    price = balances [i]
    desig = accounts [i]
    print (f'{i}. {desig} - ${price :.2f}')
print ()
 
total = sum(balances)
average = sum(balances)/len(balances)

print (f'Total: ${total :.2f}')
print (f'Average: ${average :.2f}')

hightest_balance = 0

for i in range (len(accounts)):
    desig = accounts [i]
    price = balances [i]
    if price > hightest_balance:
        hightest_balance = price
        print (f'Highest balance: {desig} - ${hightest_balance :.2f}')
print ()

change_it = 'Yes'
while change_it == 'Yes':
    print ()
    change_it = input ('Do you want to update an account? ').capitalize ()
    print()
    if change_it == 'Yes':
        index = int(input ('What account index do you want to update? '))
        new_value = int(input ('What is the new amount? '))
        balances [index] = new_value
        print ()
        print ('Account Information:')
        for i in range (len(accounts)):
            price = balances [i]
            desig = accounts [i]
            print (f'{i}. {desig} - ${price :.2f}')        
else:
    print ('Account Information:')
    for i in range (len(accounts)):
        price = balances [i]
        desig = accounts [i]
        print (f'{i}. {desig} - ${price :.2f}')