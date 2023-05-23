#Writing basic Functions
#Author: josé Quemba
print ()

def display_regular (regular):
    print (regular)

def display_uppercase (upper):
    display_uppercase_v = upper.upper ()
    print (display_uppercase_v)

def display_lowercase (lower):
    display_lowercase_v = lower.lower ()
    print (display_lowercase_v)

user_words = input ('What is your message? ')

display_regular (user_words)
display_uppercase (user_words)
display_lowercase (user_words)