#Heart rate
#Author: josé Quemba

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    #reverse and print fruit_list.
    fruit_list.reverse ()
    print(f"Reversed: {fruit_list}")

    #append "orange" to the end of fruit_list and print the list.
    fruit_list.append ("orange")
    print(f"Appended: {fruit_list}")

    #find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    find_a = fruit_list.index ("apple")
    fruit_list.insert (find_a, "cherry")
    print(f"Appended: {fruit_list}")

    #Add code to remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    #pop the last element from fruit_list and print the popped element and the list.
    fruit_list.pop ()
    print(f"Appended: {fruit_list}")

    #sort and print fruit_list.
    fruit_list.sort ()
    print(f"Appended: {fruit_list}")

    #clear and print fruit_list.
    fruit_list.clear ()
    print(f"Appended: {fruit_list}")

    
#call to the main function.
if __name__=="__main__":
    main ()