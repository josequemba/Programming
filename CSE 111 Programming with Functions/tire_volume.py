#Heart rate
#Author: josé Quemba4

import math
from datetime import datetime


print ('tire_volume.py')

#user prompts
tire_width_w = int(input ('Enter the width of the tire in mm (ex 205): '))
tire_ratio_a = int(input ('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter_d = int(input ('Enter the diameter of the wheel in inches (ex 15): '))

#the function to calculate the volume
def approximate_volume (w, a, d):
    volume = (math.pi * (w**2) * a * ((w * a) + (2540 * d))) / 10000000000 
    return volume
print ()

print (f'The approximate volume is {approximate_volume (tire_width_w, tire_ratio_a, wheel_diameter_d):.2f} liters')

#Approximated cost of the tire ------ Exceeded Requirements
if wheel_diameter_d <= 15 and wheel_diameter_d >= 1:
    price = '$50 to $133'
elif wheel_diameter_d <= 30 and wheel_diameter_d >= 16:
    price = '$134 to $217'
elif wheel_diameter_d <= 45 and wheel_diameter_d >= 17:
    price = '$218 to $300'
else:
    prece = 'more than $300'
print (f'A tire with the dimensions you entered, costs approximatedly {price}.')
print ()


#prompt if they want to buy a tire and prompt their phone nember too
user_phone = ''
if_wants_buy = input('Do you want to buy a tire with the dimensions that you entered (yes/no)? ')
if if_wants_buy.lower () == 'yes':
    user_phone = input('Please enter your phone number: ')
else:
    print ('Thanks, goodbye')

#date
current_date_and_time = datetime.now ()

#Create and appending the users info to a file called volumes.txt
with open ("volumes.txt", mode="at") as users_data:
    print (f'{current_date_and_time:%y-%m-%d}, {tire_width_w}, {tire_ratio_a}, {wheel_diameter_d}, {approximate_volume (tire_width_w, tire_ratio_a, wheel_diameter_d):.2f}', file=users_data)
    #Exceeded Requirements
    print (user_phone, file=users_data)

