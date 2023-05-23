#Heart rate
#Author: josé Quemba

import math

n_items = int(input('Enter the number of items: '))
n_i_box = int(input('Enter the number of items per box: '))

caixa = math.ceil(n_items/n_i_box)
print ()

print (f'For {n_items} items, packing {n_i_box} items in each box, you will need {caixa} boxes.')