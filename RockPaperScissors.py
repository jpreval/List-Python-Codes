"""
Code the game Rock, Papper, Scissors as one player game vs computer. 
 1) Make game playable either in terminal or jupyter.

Computer must determine who whins and ask if player wants to play again. 

"""


import random 

def game (a):
    l = ['Rock', 'Paper', 'Scissors']
    if a not in l:
        print ('Try Again')
    b = random.choice(l)
    if a == b:
        print ('we both chose'), a
    if a == 'Rock' and b == 'Paper':
        print ('Paper beats Rock, I Win')
    if a == 'Rock' and b == 'Scissors':
        print ('Rock beats Scissors, You Win')
    if a == 'Paper' and b == 'Rock':
        print ('Paper beats Rock, You Win')
    if a == 'scissors' and b == 'Paper':
        print ('Scissors beats Paper, You Win')

while True:
    play = input("Do You want to play again? YES or NO  ").lower()  
    if play == 'yes':
        a = input("Rock, Paper or Scissors  ")
        game(a)
    elif play == 'no':
        print ('Thanks for Playing')
        break
    else:
        print ('Answer should be YES or NO')
