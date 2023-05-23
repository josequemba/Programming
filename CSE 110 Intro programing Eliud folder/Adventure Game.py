print ('Welcome at my "dating over the sea - adventure" game')
print ()
kick_off = input ('To satart, please type PLAY ')
print ()
story_one = ('The great thing about a long-distance relationship is that it can help strengthen the bond that goes '
+ 'beyond the physical between you and your partner, because you have more time to talk to each other about '
+ 'yourselves and about each other. A long-distance relationship fosters communication and trust-building. '
+ 'Would you rather be in a LONG DISTANCE relationship or in a FACE TO FACE relationship?')
if kick_off.upper () == 'PLAY':
    level_1 = story_one
else:
    level_1 = ''
print (level_1)

kick_off_2 = input ()
print ()
story_two = ('A recent study published in the Journal of Communication found that people in long-distance relationships '
+ 'have stronger bonds than those in who have a more consistent face-to-face connections with their significant others. '
+ 'Researchers suspect that’s because individuals in LDR’s have to try harder to communicate, and are in turn rewarded '
+ 'with a closer bond to their significant other. This feels a little tough for us to swallow, having been in a failed '
+ 'long-distance relationship or two ourselves, over the years. The even more surprising fact from the study: that 3 '
+ 'million married couples in the U.S. live apart — meaning that even if you’re not in one now, chances are, you may find '
+ 'yourself in a far-flung romance in the future. So, with memories of our own disastrous efforts at LDRs dancing in our brains, '
+ 'we felt it was only right to look to the pros to get some solid advice on not just surviving, but thriving in, a long-distance '
+ 'relationship. Would you rather be with someone who speaks your NATIVE LANGUAGE or someone that IS LEARNING your native language? ')
story_two1 = ('Face-to-face communication is often more effective than written or audio-only conversations. ' 
+ 'This is because seeing one another allows us to pick up on nonverbal cues and body language. And because a lot of '
+ 'communication is nonverbal, being able to see each other helps us understand each other better. Would you rather be with '
+ 'someone that HAS ALREADY EVERYTHING or START FROM ZERO with your partner and build everything together?' )
if kick_off_2.upper () == 'LONG DISTANCE':
    level_2 = story_two
elif kick_off_2.upper () == 'FACE TO FACE':
    level_2 = story_two1
else:
    level_2 = ''
output = f'You chose {kick_off_2.upper ()} relationship 😁.'
print (output)
output = f'Here is what we can learn about {kick_off_2.upper ()} relationships:'
print (output)
print ()
print (level_2)

kick_off_3 = input ()
print ()
native_tongue = ("A good relationship can conquer any boundaries, including language-related ones. That said, there's always an extra "
+ "challenge when couples speak different primary languages from one another. Learning the native language of your partner is going "
+ "to put you to the test more than you'd think. It's also a sign of respect for them and their life before they met you. It's a way "
+ "to show them you care and you're interested in everything that concerns them, even the words they learned as kids.")
is_learning_native_tongue = ("6 tips from a psychologist for expats: \n1) Develop efficient communication."
+ "\n2) Don't assume your partner is your enemy. \n3) Have a safe word to stop the escalation. \n4) Find your language as a couple."
+ "\n5) Have your partner on your side. \n6) Don't set unrealistic goals.")
has_everything = ('According to a relationship expert, significant income disparity can cause strain in the relationship. '
+ 'The best way to handle potential conflict is through self-reflection, communication, and letting your partner know you '
+ 'value them for more than their money.')
start_from_zero = ('By having a relationship where you both built everything: \n1) You maintain a meaningful emotional connection '
+ 'with each other. \n2) You’re not afraid of (respectful) disagreement. \n3) You keep outside relationships and interests alive.'
+ '\n4)You communicate openly and honestly.')
if kick_off_3.upper () == 'NATIVE LANGUAGE':
    level_3 = native_tongue
elif kick_off_3.upper () == 'IS LEARNING':
    level_3 = is_learning_native_tongue
elif kick_off_3.upper () == 'HAS ALREADY EVERYTHING':
    level_3 = has_everything
elif kick_off_3.upper () == 'START FROM ZERO':
    level_3 = start_from_zero
else:
    level_3 = ''
print ('Here is what we can learn about it:')
print ()
print (level_3)