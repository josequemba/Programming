print ('Welcome to the velocity calculator. Please enter the following: ')
m_mass = input ('Mass (in kg): ')
g_gravity = input ('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ')
t_time = input ('Time (in seconds): ')
p_density = input ('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): ')
A_cross = input ('Cross sectional area (in m^2): ')
C_drag_constant = input ('Drag constant (0.5 for sphere, 1.1 for cylinder): ')
inner_value_c = (1/2) * float (p_density) * float (A_cross) * float (C_drag_constant)
print ()

output = f'The inner value of c is: {(inner_value_c) :.3f}'
print (output)

import math 
velocity_at_t_part1 = math.sqrt (float(m_mass) * float(g_gravity) / float(inner_value_c))
velocity_at_t_part2 = 1 - math.exp((- math.sqrt (float(m_mass) * float(g_gravity) * float(inner_value_c)) / float(m_mass) * float(t_time)))
output = f'The velocity after {float(t_time)} seconds is: {(velocity_at_t_part1 * velocity_at_t_part2) :.3f} m/s'
print (output)
print () 

#STRETCH CHALLENGE 01
print () 
import math
print ('Welcome to the velocity calculator for a bowling ball. Please enter the following: ')
m_mass_bowling_ball = input ('Mass (in kg): ')
g_gravity_bowling_ball = input ('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ')
t_time_bowling_ball = input ('Time (in seconds): ')
     #Calculating the Dencity of the Bowling ball
radius_bowling_ball = input ('radius (in m): ')
volume = (4/3) * math.pi * float(radius_bowling_ball) ** 3
p_density_bowling_ball = float(m_mass_bowling_ball)/volume
output = f'The density of the bowling ball is {(p_density_bowling_ball) :.3f} m^3'
print (output)
     #Calculating the Cross sectional Area of the Bowling ball
output = f'The Cross sectional area of the bowling ball is {math.pi * (float(radius_bowling_ball) ** 2) :.3f} m^2'
print (output)
C_drag_constant_bowling_ball = input ('Drag constant (0.5 for sphere): ')
inner_value_c_bowling_ball = (1/2) * float (p_density_bowling_ball) * (math.pi * (float (radius_bowling_ball) ** 2)) * float (C_drag_constant_bowling_ball)
output = f'The inner value of c is: {(inner_value_c_bowling_ball) :.3f}'
print (output)
velocity_at_t_part1_bowling_ball = math.sqrt (float(m_mass_bowling_ball) * float(g_gravity_bowling_ball) / float(inner_value_c_bowling_ball))
velocity_at_t_part2_bowling_ball = 1 - math.exp((- math.sqrt (float(m_mass_bowling_ball) * float(g_gravity_bowling_ball) * float(inner_value_c_bowling_ball)) / float(m_mass_bowling_ball) * float(t_time_bowling_ball)))
output = f'The velocity after {float(t_time_bowling_ball)} seconds is: {(velocity_at_t_part1_bowling_ball * velocity_at_t_part2_bowling_ball) :.3f} m/s'
print (output)
print () 
import math
print ('Welcome to the velocity calculator for a loaf of bread. Please enter the following: ')
m_mass_loaf_of_bread = input ('Mass (in kg): ')
g_gravity_loaf_of_bread = input ('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ')
t_time_loaf_of_bread = input ('Time (in seconds): ')
     #Calculating the Dencity of the loaf of bread (cylinder)
radius_loaf_of_bread = input ('Hight (in m): ')
hight_loaf_of_bread = input ('radius (in m): ')
volume = float(hight_loaf_of_bread) * math.pi * float(radius_loaf_of_bread) ** 2
p_density_loaf_of_bread = float(m_mass_loaf_of_bread)/volume
output = f'The density of the loaf of bread is {(p_density_loaf_of_bread) :.3f} m^3'
print (output)
     #Calculating the Cross sectional Area of the loaf of bread (cylinder)
output = f'The Cross sectional area of the loaf of bread is {math.pi * (float(radius_loaf_of_bread) ** 2) :.3f} m^2'
print (output)
C_drag_constant_loaf_of_bread = input ('Drag constant (1.1 for cylinder): ')
inner_value_c_loaf_of_bread = (1/2) * float (p_density_loaf_of_bread) * (math.pi * (float (radius_loaf_of_bread) ** 2)) * float (C_drag_constant_loaf_of_bread)
output = f'The inner value of c is: {(inner_value_c_loaf_of_bread) :.3f}'
print (output)
velocity_at_t_part1_loaf_of_bread = math.sqrt (float(m_mass_loaf_of_bread) * float(g_gravity_loaf_of_bread) / float(inner_value_c_loaf_of_bread))
velocity_at_t_part2_loaf_of_bread = 1 - math.exp((- math.sqrt (float(m_mass_loaf_of_bread) * float(g_gravity_loaf_of_bread) * float(inner_value_c_loaf_of_bread)) / float(m_mass_loaf_of_bread) * float(t_time_loaf_of_bread)))
output = f'The velocity after {float(t_time_loaf_of_bread)} seconds is: {(velocity_at_t_part1_loaf_of_bread * velocity_at_t_part2_loaf_of_bread) :.3f} m/s'
print (output)
print ()  
import math
print ('Welcome to the velocity calculator for a skydiver. Please enter the following: ')
m_mass_skydiver = input ('Mass (in kg): ')
g_gravity_skydiver = input ('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ')
t_time_skydiver = input ('Time (in seconds): ')
p_density_skydiver = input('Density of the skydiver (in km/hr, 220 spread-eagled and 320 head-down position): ')
     #Calculating the Cross sectional Area of the skydiver (Rectangle)
skydiver_length = input ('Skydiver length (facing the position they are falling): ')
skydiver_Width = input ('Skydiver width (facing the position they are falling): ')
output = f'The Cross sectional area of the skydiver is {(float(skydiver_length) * float(skydiver_Width)) :.3f} m^2'
print (output)
C_drag_constant_skydiver = input ('Drag constant (1 for spread-eagled, and 0.70 for head-down position): ')
inner_value_c_skydiver = (1/2) * float (p_density_skydiver) * (float(skydiver_length) * float(skydiver_Width)) * float (C_drag_constant_skydiver)
output = f'The inner value of c is: {(inner_value_c_skydiver) :.3f}'
print (output)
velocity_at_t_part1_skydiver = math.sqrt (float(m_mass_skydiver) * float(g_gravity_skydiver) / float(inner_value_c_skydiver))
velocity_at_t_part2_skydiver = 1 - math.exp((- math.sqrt (float(m_mass_skydiver) * float(g_gravity_skydiver) * float(inner_value_c_skydiver)) / float(m_mass_skydiver) * float(t_time_skydiver)))
output = f'The velocity after {float(t_time_skydiver)} seconds is: {(velocity_at_t_part1_skydiver * velocity_at_t_part2_skydiver) :.3f} m/s'
print (output)
print () 

#STRETCH CHALLENGE 02
print ()
print ('Welcome to the velocity calculator on Earth and on Jupiter. Please enter the following: ')
m_mass = input ('Mass (in kg): ')
g_gravity_in_earth = 9.8
g_gravity_in_jupiter = 24
t_time = input ('Time (in seconds): ')
p_density = input ('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): ')
A_cross = input ('Cross sectional area (in m^2): ')
C_drag_constant = input ('Drag constant (0.5 for sphere, 1.1 for cylinder): ')
inner_value_c = (1/2) * float (p_density) * float (A_cross) * float (C_drag_constant)
print ()

output = f'The inner value of c is: {(inner_value_c) :.3f}'
print (output)
print ()
import math 
velocity_at_t_in_earth_part1 = math.sqrt (float(m_mass) * float(g_gravity_in_earth) / float(inner_value_c))
velocity_at_t_in_earth_part2 = 1 - math.exp((- math.sqrt (float(m_mass) * float(g_gravity_in_earth) * float(inner_value_c)) / float(m_mass) * float(t_time)))
output = f'The velocity on Earth after {float(t_time)} seconds is: {(velocity_at_t_in_earth_part1 * velocity_at_t_in_earth_part2) :.3f} m/s'
print (output)
velocity_at_t_in_jupiter_part1 = math.sqrt (float(m_mass) * float(g_gravity_in_jupiter) / float(inner_value_c))
velocity_at_t_in_jupiter_part2 = 1 - math.exp((- math.sqrt (float(m_mass) * float(g_gravity_in_jupiter) * float(inner_value_c)) / float(m_mass) * float(t_time)))
output = f'The velocity on Jupiter after {float(t_time)} seconds is: {(velocity_at_t_in_jupiter_part1 * velocity_at_t_in_jupiter_part2) :.3f} m/s'
print (output)
print ()

#STRETCH CHALLENGE 03
print()
import math
print ('Calculate the Terminal velocity of a bowling ball. Please enter the following: ')
m_mass_bowling_ball_t = input ('Mass (in kg): ')
g_gravity_bowling_ball_t = input ('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ')
t_time_bowling_ball_t = input ('Time (in seconds): ')
     #Calculating the Dencity of the Bowling ball
radius_bowling_ball_t = input ('radius (in m): ')
volume_t = (4/3) * math.pi * float(radius_bowling_ball_t) ** 3
p_density_bowling_ball_t = float(m_mass_bowling_ball_t)/volume_t
output = f'The density of the bowling ball is {(p_density_bowling_ball_t) :.3f} m^3'
print (output)
     #Calculating the Cross sectional Area of the Bowling ball
output = f'The Cross sectional area of the bowling ball is {math.pi * (float(radius_bowling_ball_t) ** 2) :.3f} m^2'
print (output)
C_drag_constant_bowling_ball_t = input ('Drag constant (0.5 for sphere): ')
inner_value_c_bowling_ball_t = (1/2) * float (p_density_bowling_ball_t) * (math.pi * (float (radius_bowling_ball_t) ** 2)) * float (C_drag_constant_bowling_ball_t)
output = f'The inner value of c is: {(inner_value_c_bowling_ball_t) :.3f}'
print (output)
print ()
v_terminal = math.sqrt (float(m_mass_bowling_ball_t) * float(g_gravity_bowling_ball_t) / (1/2) * float (p_density_bowling_ball_t) * (math.pi * (float (radius_bowling_ball_t) ** 2)) * float (C_drag_constant_bowling_ball_t))
output = f'The Terminal velocity of the bowling ball after {float(t_time_bowling_ball_t)} seconds is {(v_terminal) :.3f} m/s'
print (output)



