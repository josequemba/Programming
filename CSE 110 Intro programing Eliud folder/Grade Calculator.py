student_grade = input ('Waht is you grade percent? ')
if float(student_grade) >= 90:
    letter = 'A'
elif float(student_grade) >= 80:
    letter = 'B'
elif float(student_grade) >= 70:
    letter = 'C'
elif float(student_grade) >= 60:
    letter = 'D'
else:
    letter = 'F'
output = f'Your letter grade is {letter}.'
print (output)
if float(student_grade) >= 70:
    print ('You have passed the course.')
else:
    print ('You have failed to pass the course.')
if float(student_grade) >= 70:
    print ('Congratulations for passing the course, '
        + 'keep improving your your skills.')
else:
    print ('Sorry for that, but at least now you can figure out where ' 
        + 'you made more mistakes and spend more time in getting better on those areas you made more mistakes.')

print ()

#STRETCH CHALLENGE 01 B+ or A-

last_digit = float(student_grade) % 10
if last_digit >= 7:
    math_sign = '+'
elif last_digit < 3:
    math_sign = '-'
else:
    math_sign = ''
output = f'Your letter grade is {letter + math_sign}.'
print (output)
if float(student_grade) >= 70:
    print ('You have passed the course.')
else:
    print ('You have failed to pass the course.')
if float(student_grade) >= 70:
    print ('Congratulations for passing the course, '
        + 'keep improving your your skills.')
else:
    print ('Sorry for that, but at least now you can figure out where ' 
        + 'you made more mistakes and spend more time in getting better on those areas you made more mistakes.')

print ()

#STRETCH CHALLENGE 02 no A+ grade, only A and A-.

if float(student_grade) >= 97:
    no_sign = letter
else:
    no_sign = letter + math_sign

output = f'Your letter grade is {no_sign}.'
print (output)
if float(student_grade) >= 70:
    print ('You have passed the course.')
else:
    print ('You have failed to pass the course.')
if float(student_grade) >= 70:
    print ('Congratulations for passing the course, '
        + 'keep improving your your skills.')
else:
    print ('Sorry for that, but at least now you can figure out where ' 
        + 'you made more mistakes and spend more time in getting better on those areas you made more mistakes.')

print ()

#STRETCH CHALLENGE 03 there is no F+ or F- grades, only F

if float(student_grade) >= 97:
    no_sign = letter
elif letter == 'F':
    no_sign = letter
else:
    no_sign = letter + math_sign

output = f'Your letter grade is {no_sign}.'
print (output)
if float(student_grade) >= 70:
    print ('You have passed the course.')
else:
    print ('You have failed to pass the course.')
if float(student_grade) >= 70:
    print ('Congratulations for passing the course, '
        + 'keep improving your your skills.')
else:
    print ('Sorry for that, but at least now you can figure out where ' 
        + 'you made more mistakes and spend more time in getting better on those areas you made more mistakes.')

