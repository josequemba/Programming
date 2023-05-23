Square_length=input('What is the leangth of a side of a square? ')
output=f'The area of the square is: {float(Square_length)*float(Square_length)}'
print(output)
print()
Rectangle_Length=input('What is the length of rectangle? ')
Rectangle_Width=input('What is the width of the rectangle? ')
output=f'The area of the rectangle is: {float(Rectangle_Length)*float(Rectangle_Width)}'
print(output)
print()
Circle_radius=input('What is the radius of the circle? ')
output=f'The area of the circle is:: {float(Circle_radius)**2*3.14}'
print(output)

print('The stretch challenges for this activity')
print()

print('Fisrt')
import math 
Circle_radius=input('What is the radius of the circle? ')
output=f'The area of the circle is: {math.pi*float(Circle_radius)**2}'
print(output)
print()

print('Second')
Value_for_areas=input('What is the length value that you want to calculate the area for different shapes? ')
output=f'The area of the square is: {float(Value_for_areas)*float(Value_for_areas)}'
print(output)
output=f'The area of the circle is: {float(Value_for_areas)**2*math.pi}'
print(output)
output=f'The volume of the cube is: {float(Value_for_areas)**3}'
print(output)
output=f'The volume of the sphere is: {(4/3)*math.pi*float(Value_for_areas)**3}'
print(output)
print()

print('Third')
Square_length=input('What is the leangth of a side of a square in centimeters? ')
output=f'The area of the square is: {float(Square_length)*float(Square_length)} cm^2'
print(output)
output=f'The area of the square is: {float(Square_length)*float(Square_length)/10000} m^2'
print(output)
print()
Rectangle_Length=input('What is the length of rectangle in centimeters? ')
Rectangle_Width=input('What is the width of the rectangle? ')
output=f'The area of the rectangle is: {float(Rectangle_Length)*float(Rectangle_Width)} cm^2'
print(output)
output=f'The area of the rectangle is: {float(Rectangle_Length)*float(Rectangle_Width)/10000} m^2'
print(output)
print()
Circle_radius=input('What is the radius of the circle in centimeters? ')
output=f'The area of the circle is:: {float(Circle_radius)**2*math.pi} cm^2'
print(output)
output=f'The area of the circle is:: {float(Circle_radius)**2*math.pi/10000} m^2'
print(output)