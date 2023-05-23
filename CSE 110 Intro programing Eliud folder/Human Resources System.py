#Human Resources System
#Author: josé Quemba
print ()

# Core requirements

with open ('hr_system.txt') as workers_data:
    for data in workers_data:
        split_data = data.split ()
        names = split_data [0]
        job_titles = split_data [2]
        #print (f'Name: {names}, Title: {job_titles}')

# Name: Alexia, Title: Engineer
# 01
        id_number = split_data [1]
        salary = int(split_data [3])
        #print (f'{names} (ID: {id_number}), {job_titles} - ${salary:.2f}')

# 02 & 03 
        paycheck = salary/24
        if job_titles == 'Engineer':
            paycheck_bonus = paycheck + 1000
            print (f'{names} (ID: {id_number}), {job_titles} - ${paycheck_bonus:.2f}')
        else:
            print (f'{names} (ID: {id_number}), {job_titles} - ${paycheck:.2f}')


