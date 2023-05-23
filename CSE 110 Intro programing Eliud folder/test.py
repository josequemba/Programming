#float_number = 12.234325335563
#print(round(float_number, 2))

#import datetime
#now=datetime.date.today()
#print(now)

# Finding the largest number in a list

my_list= [1,9,4,3,5,8,10]

largest = 0

for value in my_list:

    if value > largest:

        largest = value

print(f"The largest is {largest}")

# finginf the smallest number in a list

my_list= [1,9,4,3,5,8,10]

smallest = 10000

for value in my_list:

    if value < smallest:

        smallest = value

print(f"The largest is {smallest}")

books = 'Eliud'
