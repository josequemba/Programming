First_name=input('What is your first name? ')
Last_name=input('Whas is your last name? ')
Email_Address=input('Your email address? ')
Phone_Number=input('Your Phone Number? ')
Job_Title=input('Your Job Title? ')
ID_Number=input('Your ID Number? ')
Hair_color=input('What is the color of your hair? ')
Eye_color=input('What is the color of your eye? ')
Start_month=input('In What month do you started? ')
Advanced_training=input('Answer with yes/no if you have completed advanced training? ')
print()
print("Please enter the following information")
print()
print('First name:'+' '+First_name)
print('Last name:'+' '+Last_name)
print('Email Address:'+' '+Email_Address)
print('Phone Number:'+' '+Phone_Number)
print('Job Title:'+' '+Job_Title)
print('ID Number:'+' '+ID_Number)
print()
print('The ID Card is:')
print('--------------------------------------------')
output='{1}, {0}'.format(First_name.title(),Last_name.upper())
print(output)
output= Job_Title.title()
print(output)
output='ID:'+' '+ID_Number
print(output)
print()
output=Email_Address.lower()
print(output)
output=Phone_Number
print(output)
#output='Hair:'+' '+Hair_color.ljust(20)+'Eyes:'+' '+Eye_color
#print(output)
#output='Month:'+' '+Start_month.ljust(20)+'Training:'+' '+Advanced_training
#print(output)
output='Hair:'+' '+Hair_color+'\t'+'Eyes:'+' '+Eye_color.expandtabs(70)
print(output)
output='Month:'+' '+Start_month+'\t'+'Training:'+' '+Advanced_training.expandtabs(70)
print(output)
print('--------------------------------------------')