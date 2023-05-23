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
            total_data_country += country.count (user_country.capitalize ())
            average_country = total_country/total_data_country 
    print (total_data_country)


