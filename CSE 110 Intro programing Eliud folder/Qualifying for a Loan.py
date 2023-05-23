print ('Welcome to QFL')
print ('QFL will help you to know if you are eligible to take a loan or not')
print ('To know if you are eligible for a loan QFL needs a couple of information that will help it to check your eligibility')
print ('In a scale of 1 - 10 rate the following:')
large = float (input ('How large is the loan? '))
good_credit = float (input ('How good is your credit history? '))
high_income = float (input ('How high is your income? '))
down_payment = float (input ('How large is your down payment? '))
print ()
if large >= 5: 
    if good_credit >= 7 and high_income >= 7:
        decision = 'Yes'
    elif good_credit >= 7 or high_income >= 7:
        if down_payment >= 5:
            decision = 'Yes'
        else:
            decision = 'No' 
    else:
        decision = 'No'
else:
    if good_credit < 4:
        decision = 'No' 
    else:
        if high_income >= 7 or down_payment >= 7:
            decision = 'Yes'
        elif high_income >= 4 and down_payment >= 4:
            decision = 'Yes'
        else:
            decision = 'No' 
if decision == 'Yes':
    print ('Congratulations you are eligible for the loan')
else:
    print ('Unfortunatly you are not eligible for the loan')