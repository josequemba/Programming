#Heart rate
#Author: josé Quemba
print ()


def main ():
    
    #reading and printing the list
    provinces = provinces_list("C:\\Users\\Jose Eliud Dias\\Desktop\\Programming\\CSE 111 Programming with Functions\\provinces.txt")
    #print (provinces)

    #Remove the first element from the list.
    provinces.pop(0)

    #Remove the last element from the list.
    provinces.pop ()

    #Replace all occurrences of "AB" in the list with "Alberta".
    for i in range(len(provinces)):
        if provinces [i] == "AB":
            provinces [i] = "Alberta"
    print (provinces)

    print ()
    #Count the number of elements that are "Alberta" and print that number.
    alberta_number = 0
    for i in range(len(provinces)):
        if provinces [i] == "Alberta":
            alberta_number += 1
        
    print(f'The name Alberta is reapeted {alberta_number} times.')

def provinces_list (list_in_txt):

    province = []

    #openning the file "provinces.txt"
    with open (list_in_txt, "rt") as canadian_provinces:
        for provinces_list in canadian_provinces:
            provinces = provinces_list.strip ()
           
            #adding to the provinces_list
            province.append(provinces)

    return province

if __name__ == "__main__":
    main ()
