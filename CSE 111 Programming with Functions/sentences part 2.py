#Heart rate
#Author: josé Quemba

print()
import random

def main ():
    single = 1
    plural = 2
    past = 'past'
    present = 'present'
    future = 'future'

    sentence_1 = make_sentence (single, past)
    sentence_2 = make_sentence (single, present)
    sentence_3 = make_sentence (single, future)
    sentence_4 = make_sentence (plural, past)
    sentence_5 = make_sentence (plural, present)
    sentence_6 = make_sentence (plural, future)

    print (sentence_1)
    print (sentence_2)
    print (sentence_3)
    print (sentence_4)
    print (sentence_5)
    print (sentence_6)

def make_sentence(quantity, tense):
    determiner = get_determiner (quantity)
    cap_word = determiner.capitalize ()
    noun = get_noun (quantity)
    verb = get_verb (quantity, tense)

    # another call to a second get_prepositional_phrase so that each sentence includes two prepositional for exceeding the Requirements
    prepo_phrase = get_prepositional_phrase (quantity)
    sec_prepo_phrase = get_prepositional_phrase (quantity)

    sentence = (f'{cap_word} {noun} {prepo_phrase} {verb} {sec_prepo_phrase}.')
    return sentence

def get_determiner (quantity):
    if quantity == 1:
        determiner = ["a", "one", "the"]
    else:
        determiner = ["some", "many", "the"]
    determiner_choice = random.choice(determiner)
    return determiner_choice

def get_noun(quantity):
    if quantity == 1:
        determiner = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        determiner = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    determiner_choice = random.choice(determiner)
    return determiner_choice

def get_verb(quantity, tense):
    if tense.lower () == 'past':
        pick = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense.lower () == 'present' and quantity == 1:
        pick = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif tense.lower () == 'present' and quantity != 1:
        pick = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense.lower () == 'future':
        pick = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", 
            "will talk","will walk", "will write"]
    pick = random.choice(pick)
    return pick

def get_preposition ():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    pick_randomly = random.choice (prepositions)
    return pick_randomly

def get_prepositional_phrase (quantity):
    prepo = get_preposition ()
    deter = get_determiner (quantity)
    noun = get_noun (quantity)
    sentence = (f'{prepo} {deter} {noun}')
    return sentence

main ()
print ()