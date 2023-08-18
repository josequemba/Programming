#Heart rate
#Author: josé Quemba
print ()

print ('This program is an implementation of the Rosenberg \nSelf-Esteem' 
       +' Scale. This program will show you ten \nstatements that you could possibly'
       +' apply to yourself. \nPlease rate how much you agree with each of'
       +' the \nstatements by responding with one of these four letters:')

print ()

print ('D means you strongly disagree with the statement.')
print ('d means you disagree with the statement.')
print ('a means you agree with the statement.')
print ('A means you strongly agree with the statement.')

print ()

def main ():
   
    worth = input ("1. I feel that I am a person of worth, at least on an equal plane with others. \nEnter D, d, a, or A: ")

    qualities = input ("2. I feel that I have a number of good qualities. \nEnter D, d, a, or A: ")

    all_in_all = input ("3. All in all, I am inclined to feel that I am a failure. \nEnter D, d, a, or A: ")

    average_do = input ("4. I am able to do things as well as most other people. \nEnter D, d, a, or A: ")

    not_proud = input ("5. I feel I do not have much to be proud of. \nEnter D, d, a, or A: ")
    
    attitude = input ("6. I take a positive attitude toward myself. \nEnter D, d, a, or A: ")
   
    satisfaction = input ("7. On the whole, I am satisfied with myself. \nEnter D, d, a, or A: ")
   
    self_respect = input ("8. I wish I could have more respect for myself. \nEnter D, d, a, or A: ")

    feeling_useless = input ("9. I certainly feel useless at times. \nEnter D, d, a, or A: ")

    good_at_all = input ("10. At times I think I am no good at all. \nEnter D, d, a, or A: ")

    total_score = (score_calculator_1_2_4_6_7 (worth) + score_calculator_1_2_4_6_7 (qualities) + score_calculator_1_2_4_6_7 (average_do) 
    + score_calculator_1_2_4_6_7 (attitude) + score_calculator_1_2_4_6_7 (satisfaction) #end of the 1_2_4_6_7
    + score_calculator_3_5_8_9_10 (all_in_all) + score_calculator_3_5_8_9_10 (not_proud) + score_calculator_3_5_8_9_10 (self_respect)
    + score_calculator_3_5_8_9_10 (feeling_useless) + score_calculator_3_5_8_9_10 (good_at_all))  #end of the 3_5_8_9_10
    
    print()
    print (f'Your score is {total_score}.')
    print ('A score below 15 may indicate problematic low self-esteem.')
    print ()

def score_calculator_1_2_4_6_7 (user):
    score = 0
    if user == 'D':
        score += 0
    elif user == 'd':
        score += 1
    elif user == 'a':
        score += 2
    elif user == 'A':
        score += 3
    return score

def score_calculator_3_5_8_9_10 (user):
    score = 0
    if user == 'D':
        score += 3
    elif user == 'd':
        score += 2
    elif user == 'a':
        score += 1
    elif user == 'A':
        score += 0
    return score

if __name__ == "__main__":
    main()