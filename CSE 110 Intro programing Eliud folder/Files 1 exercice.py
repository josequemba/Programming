#Multiple lists Strecth Challenge
#Shopping cart along with their prices
#Author: josé Quemba
print ()

with open ('books.txt') as name_of_books:
    for books in name_of_books:
        not_space = books.strip ()
        print (f'{not_space}')