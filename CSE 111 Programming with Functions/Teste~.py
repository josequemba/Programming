from datetime import datetime

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#print (weekday [6])

#user = int(input('day: '))
#for i in range(len(weekday)):
#    position = weekday [i]
#    print (f'{position}')

print ()

#for i, word in enumerate(weekday):
 #   if user == i:
  #      print (word)


def kilometers_from_miles(miles):

   # miles = float(input("Please enter a distance in miles: "))
    km = miles * 1.60934
    return km

df = kilometers_from_miles (6.9)
#print (df)

#------------------------------------------------------------------------------

user = "Quemba; Jose"
split = user.split ('; ')
lenh = split[0] + split[1]
enu = len (lenh)
print (enu)
number_str = len(split)
print (number_str)