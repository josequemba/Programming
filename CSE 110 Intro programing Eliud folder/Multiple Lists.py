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
    print (f'{desig} - ${price :.2f}')
print ()
 
total = sum(price)
average = sum(balances)/len(balances)

print (f'Total: ${total :.2f}')
print (f'Average: ${average :.2f}')

