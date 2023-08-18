#Heart rate
#Author: josé Quemba

print ('Welcome to this heart rate calculater')
print ('This will healp you know which heart rate when exercising are best to strengthen your heart.')
print ()
print ('When you physically exercise to strengthen your heart, you ' + 
       'should maintain your heart rate within a range for at least 20 ' +
       'minutes. To find that range, subtract your age from 220. This ' + 
       'difference is your maximum heart rate per minute. Your heart ' + 
       'simply will not beat faster than this maximum (220 - age). ' +
       'When exercising to strengthen your heart, you should keep your ' + 
       "heart rate between 65% and 85% of your heart’s maximum rate.")
print ()

user_age = int(input ('Please enter your age: '))

def max_heart_rate (age):
    max = 220 - age
    return max

def max_exercise (value):
    max = value * 85 / 100
    return max

def min_exercise (value):
    min = value * 65 / 100
    return min

user_max_rate = max_heart_rate (user_age)
exercise_min_range = min_exercise (user_max_rate)
exercie_max_range = max_exercise (user_max_rate)

output = f'When you exercise to strengthen your heart, you should keep your heart rate between {exercise_min_range} and {exercie_max_range} beats per minute.'
print (output)
