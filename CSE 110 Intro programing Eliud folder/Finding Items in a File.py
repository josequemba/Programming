#Finding Items in a File
#Author: josé Quemba4
#organized in:
# Book - Number of chapters - set of Scripture
print ()

largest_number_chapters = 0
book_largest_number = ""
scripture_refered = ""

largest_number_chapters1 = 0
book_largest_number1 = ""


print ('Learn more about the scripture you like:')
print()
user_interest = str(input ('Which volume of scriptures would you like to learn about? '))
print ()
with open ('books_and_chapters.txt') as data:
    for sets in data:
        part_sets = sets.split (':')
        book = part_sets [0].strip ()
        number_of_chapters = int(part_sets [1])
        set_of_scripture = str(part_sets [2].strip ())  
        #largest chapter
        #if number_of_chapters > largest_number_chapters:
            #largest_number_chapters = number_of_chapters

            #book_largest_number = book

            #scripture_refered = set_of_scripture
    #print (f'The Book that contains more chapters is the book of {book_largest_number} \nwith {largest_number_chapters} chapters and we can find this book \nin the scripture of the {scripture_refered}')

# STRETCH CHALLENGE------------------------------------------------------------------------------------------------------------------------------

# 01 only prints the books in the Book of Mormon
        #if set_of_scripture == 'Book of Mormon':
            #print (f'Scripture: {set_of_scripture}, Book: {book}, Chapters: {number_of_chapters}')

# 02 Find the book in the Book of Mormon that has the largest number of chapters-----------------------------------------------------------------          
            #if number_of_chapters > largest_number_chapters1:
                #largest_number_chapters1 = number_of_chapters                
                #book_largest_number1 = book
    #print (f'In The Book of Mormon, the Book that contains more chapters is the book of {book_largest_number1} \nwith {largest_number_chapters1} chapters')    

# 03 ask the user which volume of scriptures they would like to learn about----------------------------------------------------------------------
        if set_of_scripture.upper () == user_interest.upper ():
            print (f'Scripture: {set_of_scripture}, Book: {book}, Chapters: {number_of_chapters}')
            print ()
            if number_of_chapters > largest_number_chapters1:
                largest_number_chapters1 = number_of_chapters                
                book_largest_number1 = book
    print (f'The Book that contains more chapters is the book of {book_largest_number1} \nwith {largest_number_chapters1} chapters')