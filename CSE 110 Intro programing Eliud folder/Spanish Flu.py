# Assignment Milestone
#Author: josé Quemba
print ()

import pandas as pd

chart = pd.read_csv ('life-expectancy.csv')
life_years = chart ['Life expectancy (years)']
country = chart ['Entity']
year = chart ['Year']
#print (f'The overall max life expectancy is: {max(life_years)}')
#print (f'The overall min life expectancy is: {min(life_years)}')
print (chart)
