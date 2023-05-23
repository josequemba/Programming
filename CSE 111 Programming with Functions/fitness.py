#Heart rate
#Author: josé Quemba
print () 

from datetime import datetime


def main():

    gender = input('Please enter your gender (M or F): ')
    birthday = input('Enter your birthdate (YYYY-MM-DD): ')
    weight = float(input('Enter your weight in U.S. pounds: '))
    height = float(input('Enter your height in U.S. inches: '))

    age = compute_age (birthday)
    weight_in_Kg = kg_from_lb (weight)
    height_in_cm = cm_from_in (height)
    bmi = body_mass_index (weight, height)
    bmr = basal_metabolic_rate (gender, weight, height, age)
    print ()

    print (f'Age (years): {age}')
    print (f'Weight (kg): {weight_in_Kg:.2f}')
    print (f'Height (cm): {height_in_cm:.1f}')
    print (f'Body mass index: {bmi:.1f}')
    print (f'Basal metabolic rate (kcal/day): {bmr:.0f}')
    pass

def compute_age(birthday):
    birthdate = datetime.strptime(birthday, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years


def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg


def cm_from_in(inches):
    cm = inches * 2.54
    return cm


def body_mass_index(weight, height):
    bmi = 10000 * (weight * 0.45359237) / (height * 2.54) ** 2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    if gender.upper () == 'F':
        bmr = 447.593 + 9.247 * (weight * 0.45359237) + 3.098 * (height * 2.54) - 4.330 * age
    elif gender.upper () == 'M':
        bmr = 88.362 + 13.397 * (weight * 0.45359237) + 4.799 * (height * 2.54) - 5.677 * age
    return bmr

main ()
