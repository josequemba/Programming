#Heart rate
#Author: josé Quemba
import csv
print ()

def main ():
    
    students_dict = read_dictionary ("C:\\Users\\Jose Eliud Dias\\Desktop\\Programming\\CSE 111 Programming with Functions\\students.csv")

    # getting an I-number form the user
    user_i_d = input('Enter an I-Number: ')

    number =  students_dict.length 
    print (number)

    # finding the student name of the I-Number entered by the user
    
    if user_i_d in students_dict:
        access_data = students_dict [user_i_d]

        name = access_data
    
        print (name)
    else:
        print ('No such student')

def read_dictionary(filename):
    I_NUMBER = 0
    NAME = 1

    # Dictionary
    students_dict = {}
    
    with open (filename, "rt") as data:
        reader = csv.reader (data)

        #skip to read the fisrt row
        next (reader)

        for dict in reader:

            key = dict [I_NUMBER]
            Value = dict [NAME]

            students_dict [key] = Value

    return students_dict

if __name__ == "__main__":
    main ()
