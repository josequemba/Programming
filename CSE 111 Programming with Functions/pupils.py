#Heart rate
#Author: josé Quemba
import csv

GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main ():
    # Each row in the pupils.csv file contains three elements.
    # These are the indexes of the elements in each row.
    #try:
        students_list = read_compound_list("C:\\Users\\Jose Eliud Dias\\Desktop\\Programming\\CSE 111 Programming with Functions\\pupils.csv")
        print (students_list)

        print ()

        extract_birthdata = lambda students_list: students_list [BIRTHDATE_INDEX]

        sorted_list = sorted (students_list, key = extract_birthdata)

        print_list (sorted_list)

    #except 
def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list (list_par):
    """this function prints each element of the list on a 
    separate line In other words, this print_list function 
    should include a for loop that prints each element on 
    a separate line.

    parameter:a list"""

    for info in list_par:
        new_list = info

        print (new_list)

if __name__ == "__main__":
    main ()