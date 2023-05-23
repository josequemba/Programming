print ('Author: José Quemba')
print ('Assignment: Amusement Park Rides')
print ()
print ()
print ('Check you are eligiable for to ride by entering the following:')
print()

first_rider_age = float (input ('What is the age of the first rider? '))
first_rider_height = float (input ('What is the height of the first rider? '))
if_a_second_rider_exist = input ('Is there a second rider (yes/no) ?')

if first_rider_height < 36:
    print ('Sorry, you may not ride.')
elif if_a_second_rider_exist.upper () == 'YES':
    second_rider_age = float (input ('What is the age of the second rider? '))
    second_rider_height = float (input ('What is the height of the second rider? '))
    if second_rider_height < 36:
        print ('Sorry, you may not ride.')
    elif first_rider_age >= 18 or second_rider_age >= 18:
        print ('Welcome to the ride. Please be safe and have fun!') 
    elif second_rider_age >= 18 and second_rider_height >= 62:
        print ('Welcome to the ride. Please be safe and have fun!') 
elif if_a_second_rider_exist.upper () == 'NO' and first_rider_age >= 18 and first_rider_height >= 62:
    print ('Welcome to the ride. Please be safe and have fun!')
else:
    print ('Sorry, you may not ride.')
    


    #Strecth Activity


first_rider_age = float (input ('What is the age of the first rider? '))
first_rider_height = float (input ('What is the height of the first rider? '))
if_a_second_rider_exist = input ('Is there a second rider (yes/no) ?')

if first_rider_height < 36:
    print ('Sorry, you may not ride.')
elif if_a_second_rider_exist.upper () == 'YES':
    second_rider_age = float (input ('What is the age of the second rider? '))
    second_rider_height = float (input ('What is the height of the second rider? '))
    if second_rider_height < 36:
        print ('Sorry, you may not ride.')
    elif first_rider_age >= 18 or second_rider_age >= 18:
        print ('Welcome to the ride. Please be safe and have fun!') 
    elif first_rider_age >= 18 or second_rider_age >= 18 and second_rider_height >= 62:
        print ('Welcome to the ride. Please be safe and have fun!')

            #stretch 01
    elif first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height >= 52:
        print ('Welcome to the ride. Please be safe and have fun!')
    
            #stretch 03
    elif first_rider_age >= 16 and second_rider_age >= 14 or first_rider_age >= 14 and second_rider_age >= 16:
        print ('Welcome to the ride. Please be safe and have fun!')
    
            #stretch 02
    elif first_rider_age >= 12 and first_rider_age <= 17 and if_a_second_rider_exist.upper () == 'YES':
        golden_passaport = input ('Does the first driver have a golden passpot? ')
        if golden_passaport.upper () == 'YES':
            print ('Welcome to the ride. Please be safe and have fun!')
        else:
            golden_passaport = input ('Does the second driver have a golden passpot? ')
            if golden_passaport.upper () == 'YES':
                print ('Welcome to the ride. Please be safe and have fun!')
            else:
                print ('Sorry, you may not ride.')
    elif if_a_second_rider_exist.upper () == 'YES'and second_rider_age >= 12 and second_rider_age <= 17 and second_rider_height >= 62:
        golden_passaport = input ('Does the second driver have a golden passpot? ')
        if golden_passaport.upper () == 'YES':
            print ('Welcome to the ride. Please be safe and have fun!')
    elif if_a_second_rider_exist.upper () == 'YES'and second_rider_age >= 12 and second_rider_age <= 17:
        golden_passaport = input ('Does the second driver have a golden passpot? ')
        if golden_passaport.upper () == 'YES':
            print ('Welcome to the ride. Please be safe and have fun!')
        else:
            print ('Sorry, you may not ride.')  

elif if_a_second_rider_exist.upper () == 'NO' and first_rider_age >= 18 and first_rider_height >= 62:
    print ('Welcome to the ride. Please be safe and have fun!')

            #stretch 02
elif first_rider_age >= 12 and first_rider_age <= 17 and first_rider_height >= 62:
    golden_passaport = input ('Does the first driver have a golden passpot? ')
    if golden_passaport.upper () == 'YES':
        print ('Welcome to the ride. Please be safe and have fun!')
    else:
        print ('Sorry, you may not ride.')
else:
    print ('Sorry, you may not ride.')