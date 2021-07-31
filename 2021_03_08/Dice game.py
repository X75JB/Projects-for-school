#A dice game
#Jackson Blackman
#2021_03_08

from time import sleep
import random


#Intro + start/quit
print('Welcome, this game is called "highest count wins" each player rolls 3 die and the person with the highest count wins.')
print()
while True:
    start_stop = str(input('Would you like to re/start or quit? (S/Q)'))
    if start_stop == 'S' or start_stop == 's':

    #Starting process
        print()
        print('Rolling...')
        sleep(1)
        print()

    #Player 1 rolls
        p1number1 = random.randint(1, 6)
        p1number2 = random.randint(1, 6)
        p1number3 = random.randint(1, 6)
        print('Player one has rolled',p1number1,p1number2,p1number3)
        print()

    #Player 2 rolls
        p2number1 = random.randint(1, 6)
        p2number2 = random.randint(1, 6)
        p2number3 = random.randint(1, 6)
        print('Player two has rolled', p2number1, p2number2, p2number3)
        print()

    #Player totals

        player1total = p1number1 + p1number2 + p1number3
        player2total = p2number1 + p2number2 + p2number3

    #Deciding winner and or draw

        if player1total > player2total:
            print('player one wins')
            print()
        elif player1total < player2total:
            print('player two wins')
            print()
        elif player1total == player2total:
            print('Draw')
            print()

    #Quitting process
    elif start_stop == 'Q' or start_stop == 'q':
        quit()

    else:
        print()
        print('Not a valid response, please enter "S" or "Q".')
        print()