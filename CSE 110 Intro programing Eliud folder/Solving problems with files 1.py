#Solving problems with files 1
#Shopping cart along with their prices
#Author: josé Quemba

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

younger_age = 10000000000
younger_person = ""

for data_set in people:
    part_data = data_set.split ()
    age = int(part_data [1])
    names = part_data [0]
    
    if age < younger_age:
        younger_age = age

        younger_person = names

print (f'The youngest person is {younger_person} with the age of {younger_age}')