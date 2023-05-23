#life-expectancy.csv
#Author: josé Quemba4
#organized in:
# Book - Number of chapters - set of Scripture
#Entity,Code,Year,Life expectancy (years)
print ()

largest_number = 0
min_number = 10000000000
country_largest = ""
year_largest = ""
country_min = ""
year_min = ""

year_user = (input ('Enter the year of interest: '))
print ()

with open ('life-expectancy.csv') as data_set:
    for data in data_set:
        part_data = data.split (',')
        country = part_data [0] 
        code = part_data [1]
        year = part_data [2]
        life_expectancy = float(part_data [3])
        #max overall
        if life_expectancy > largest_number:
            largest_number = life_expectancy

            country_largest = country

            year_largest = year
        #min overal
        if life_expectancy < min_number:
            min_number = life_expectancy

            country_min = country

            year_min = year
    print (f'The overall max life expectancy is: {largest_number} from {country_largest} in {year_largest}')
    print (f'The overall min life expectancy is: {min_number} from {country_min} in {year_min}')
    print ()
    print (f'For the year {year_user}:')

average_expectancy = ""
max_expectancy = 0
min_expectancy = 100000000000000
max_country = ""
min_country = ""
total_life = 0
total_life_data = 0
average_expectancy = 0

with open (r"C:\Users\Jose Eliud Dias\Desktop\Programming\CSE 110 Intro programing Eliud folder\life-expectancy.csv") as data_set:
    for data in data_set:
        part_data = data.split (',')
        country = part_data [0] 
        code = part_data [1]
        year = part_data [2]
        life_expectancy = float(part_data [3].strip())

        #finding to the total of life expectancy
        total_life = total_life + life_expectancy
        #finding the total of data so we can divide total of life expectancy by it and find the average
        count = data.count (',')/3
        total_life_data = total_life_data + count
        #Finding the Average
        average_expectancy = total_life/total_life_data

        if year == year_user:
        #max on that year
            if life_expectancy > max_expectancy:
                max_expectancy = life_expectancy

                max_country = country

        #min on that year
            if life_expectancy < min_expectancy:
                min_expectancy = life_expectancy

                min_country= country
    print (f'The average life expectancy across all countries was {average_expectancy:.2f}')
    print (f'The max life expectancy was in {max_country} with {max_expectancy}')
    print (f'The min life expectancy was in {min_country} with {min_expectancy}')

# user pick a country
print()
user_country = input ('type the name of a country you would like to learn about: ')

average_exp_country = ""
max_exp_country = 0
min_exp_country= 100000000000000
max_year = ""
min_year = ""

total_country = 0
total_data_country = 0
average_country = 0

with open ('life-expectancy.csv') as data_set:
    for data in data_set:
        part_data = data.split (',')
        country = part_data [0] 
        code = part_data [1]
        year = part_data [2]
        life_expectancy = float(part_data [3].strip())

        if country.lower () == user_country.lower ():
            total_country += life_expectancy
            total_data_country += country.lower ().count (user_country.lower ())
            average_country = total_country/total_data_country

        #max on that year
            if life_expectancy > max_exp_country:
                max_exp_country = life_expectancy

                max_year = year

        #min on that year
            if life_expectancy < min_exp_country:
                min_exp_country = life_expectancy

                min_year = year
    print (f'The average life expectancy across {user_country} was {average_country:.2f}')
    print (f'The max life expectancy was in {max_year} with {max_exp_country}')
    print (f'The min life expectancy was in {min_year} with {min_exp_country}')