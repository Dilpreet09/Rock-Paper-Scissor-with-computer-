#Rock paper Scissor game with computer
print ('welcome to ROCK PAPER SCISSOR')
print ('Inputs are as follows :-')
print ('1: ROCK')
print ('2: PAPER')
print ('3: SCISSOR')
player_1 = int(input('Enter Input Player1 : '))
import random
computer = random.randrange(1,4)
if player_1 == 1 and computer == 1:
    print ("Ohhh! It's a tie as computer was {}.".format(computer))
elif player_1 == 2 and computer == 2:
    print ("Ohhh! It's a tie as computer was {}.".format(computer))
elif player_1 == 3 and computer == 3:
    print ("Ohhh! It's a tie as computer was {}.".format(computer))
elif player_1 == 1 and computer == 2:
    print ("Hurry! computer wins as it was {}.".format(computer))
elif player_1 == 1 and computer == 3:
    print ("Hurry! player1 wins as computer was {}.".format(computer))
elif player_1 == 2 and computer == 1:
    print ("Hurry! player1 wins as computer was {}.".format(computer))
elif player_1 == 2 and computer == 3:
    print ("Hurry! computer wins as it was {}.".format(computer))
elif player_1 == 3 and computer == 1:
    print ("Hurry! computer wins as it was {}.".format(computer))
elif player_1 == 3 and computer == 2:
    print ("Hurry! computer wins as it was {}.".format(computer))