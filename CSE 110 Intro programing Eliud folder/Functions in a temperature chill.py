#Wind Chill Calculations
#Author: josé Quemba4
print ()
print ("Wind Chill Calculator:")

#functions
def wind_chill (T,V):
    windchill = 35.74 + (0.6215 * T) - 35.75 * (V**0.16) + (0.4275 * T * (V**0.16))
    return windchill

def celsius_to_Fahrenheit (C):
    Celsius = C * (9/5) + 32
    return Celsius

def windchill (T_type, T, V=0):
    calcule = 0
    if T_type == 'F':
        calcule = wind_chill (T, V)
    elif T_type == 'C':
        calcule = celsius_to_Fahrenheit (T)
    return calcule

# user prompts
t_user = float(input ('What is the temperature? '))
t_type = input ('Fahrenheit or Celsius (F/C)? ')
t_type = t_type.upper ()

for number in range (5,61,5):
    velocity = float(number)

    # Showing the temperature in Fahrenheits only and different velocities
    if t_type == 'F':
        temperature = t_user

        wind_chill_f = windchill (t_type, t_user, velocity)

        print (f'At temperature {temperature :.2f}F, and wind speed {number}mph, the windchill is: {wind_chill_f:.2f}F')

    elif t_type == 'C':
        temperature = windchill (t_type, t_user)
        
        wind_chill_c = windchill ('F', temperature, velocity)

        print (f'At temperature {temperature :.2f}F, and wind speed {number}mph, the windchill is: {wind_chill_c:.2f}F')
print ()