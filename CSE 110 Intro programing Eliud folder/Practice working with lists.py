#Practice working with lists
#Author: josé Quemba
print ()
name_user = []
name = ''
while name.upper () != 'END':
    name = input ('Type the name of a friend: ')
    name_user.append (name)

for name in name_user:
    print (name)