# practice 01
positive_number = int(input ('Please type a positive number: '))

while positive_number < 0:
    print ('Sorry, that is a negative number. Please try again.')
    positive_number = int(input ('Please type a positive number: '))

output = f'The number is: {positive_number}'
print (output)

# practice 02

candy = input ('May I have a piece of candy (yes/no)? ')

while candy.upper () != 'YES':
    candy = input ('May I have a piece of candy (yes/no)? ')
else:
    print ('Thank you.')
