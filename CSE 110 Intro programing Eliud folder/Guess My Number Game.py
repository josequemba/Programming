magic_number = int(input ('What is the magic number? '))
guess = int(input ('What is your guess? '))

if magic_number > guess:
    print ('Higher')
elif magic_number < guess:
    print ('Lower')
else:
    print ('You guessed it!')
print ()

# adding loop 02

magic_number2 = int(input ('What is the magic number? '))
guess2 = int(input ('What is your guess? '))

while magic_number2 > guess2 or magic_number2 < guess2:
    if magic_number2 > guess2:
        print ('Higher')
        guess2 = int(input ('What is your guess? '))
    elif magic_number2 < guess2:
        print ('Lower')
        guess2 = int(input ('What is your guess? '))
else:
    print ('You guessed it!')
print ()

# import the random library 03

import random
magic_number2 = random.randint (1,26)
guess2 = int(input ('What is your guess? '))

while magic_number2 > guess2 or magic_number2 < guess2:
    if magic_number2 > guess2:
        print ('Higher')
        guess2 = int(input ('What is your guess? '))
    elif magic_number2 < guess2:
        print ('Lower')
        guess2 = int(input ('What is your guess? '))
else:
    print ('You guessed it!')
print ()

# STRETCH CHALLENGE 01 and 02

import random

repeat = 'yes'
while repeat.upper () == 'YES':
    magic_number2 = random.randint (1,26)
    count_loop = 0
    guess2 = -1
    while guess2 != magic_number2:
        guess2 = int(input ('What is your guess? '))
        count_loop = count_loop + 1
        if magic_number2 > guess2:
            print ('Higher')
        elif magic_number2 < guess2:
            print ('Lower')
        else: 
            print ('You guessed it!')
            output = f'You attempted {count_loop} to guess the right number.'
            print (output)
            repeat = input ('Would you like to play again (yes/no)?')
else:
    print ('Thanks for playing')


