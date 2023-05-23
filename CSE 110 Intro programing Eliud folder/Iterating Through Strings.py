#07 Prove: Assignment Milestone
#Author: josé Quemba
print ()

# 01 Create a string variable to hold the word "Commitment"
word = "Commitment"
for letter in word:
    if letter == 'm':
        print (letter.upper ())
    else:
        print (letter.lower ())
print ()

# 02
user_choice = input ('What is your favorite letter? ')
for letter in word:
    if letter.lower () == user_choice.lower ():
        print (letter.upper (), end="")
    else:
        print (letter.lower (), end="")
print ()

# 03 Change the program, so that instead of capitalizing the user's favorite letter, it "hides" it, and replaces it with an underscore in the display.
user_choice = input ('What is your favorite letter? ')
for letter in word:
    if letter.lower () == user_choice.lower ():
        print ('_', end="")
    else:
        print (letter.lower (), end="")
print ()

# 01 STRETCH CHALLENGE 
user_number = int(input ('Please enter a number: '))
quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
for i, letter in enumerate (quote):
    if i % user_number == 0:
        print (letter.upper (), end="")
    else:
        print (letter.lower (), end="")
print ()

# 02 STRETCH CHALLENGE 
quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
continue_user = 'yes'
while continue_user == 'yes':
    user_number = int(input ('Please enter a number: ')) 
    for i, letter in enumerate (quote):
        if i % user_number == 0:
            print (letter.upper (), end="")
        else:
            print (letter.lower (), end="")
    print()
    continue_user = input ('Would you like to enter another number ?').lower ()
print ('Thanks, have a good one')