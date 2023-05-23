#List of numbers
#Author: josé Quemba
print ()

numbers = []
finish_user = ''

print ('Enter a list of numbers, type 0 when finished.')

while finish_user != 0:
    finish_user = int(input ('Enter number: '))
    numbers.append (finish_user)
else:
    output = f'The sum is: {sum(numbers)}'
    print (output)
    output = f'The average is: {float(sum(numbers)/(len(numbers)-1))}'
    print (output)
    output = f'The largest number is: {max(numbers)}'
    print (output)
# STRETCH CHALLENGE
    for number in numbers:
        if number > 0 and number < 100000000000:
            small = number
    print (f'The smallest positive number is: {small}')
    
    sorting = sorted (numbers)
    print ('The sorted list is:')
    for number in sorting:
        if number != 0:
            print (number)