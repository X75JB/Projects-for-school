# Alien defence game
# Jackson Blackman
# 2021_03_08

import sys
import os
import time
from time import sleep

count = 2


# Intro point
print("                                      --------------------------------------------------")
print("                                      |       GLOBAL DEFENSE, AN ALIEN KILLING GAME    | ")
print("                                      --------------------------------------------------")
print()
print()
print()
print()
print()
print("Quickly! Aliens are invading the planet.")
print("You need to activate the Global Defence Network.")
print("Hope you know the password, for Earth's sake...")
print("If the aliens outnumber humans, we are doomed!")
print()
print()
sleep(15)
os.system('cls')
start_quit = str(input(
    '                                      Will you accept the fate or will your run (A - accept, R - run):')).lower()

# Starting the game
while True:
    if start_quit == 'a':
        os.system('cls')
        password = str(input(
            '                                      Welcome to the central defence agency\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n           Please input the password:')).lower()
        os.system('cls')

        # If password is correct
        if password == 'aliens':
            print(
                '                                      [ ]Space laser activation\n                                      [ ]Anti-alien Weapons\n                                      [ ]Nukes')
            sleep(2)
            print()
            os.system('cls')
            print(
                '                                      [ ]Space laser activation\n                                      [X]Anti-alien Weapons\n                                      [ ]Nukes')
            sleep(2)
            print()
            os.system('cls')


            def print_slow(str):
                for letter in str:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.0000001)


            print_slow(
                "                                           _.-^^---....,,--\n                                       _--                  --_\n                                      <                        >\n                                      |                         |\n                                       \._                   _./\n                                          ```--. . , ; .--'''\n                                                | |   |\n                                             .-=||  | |=-.\n                                             `-=#$%&%$#=-'\n                                                | ;  :|\n                                     ('_____.,-#%&$@%#&#~,._____')")
            sleep(5)

            os.system('cls')
            print('                                      The aliens have been removed from earth. Stay safe.')
            sleep(4)
            print('\n\n                                 Terminating in 3...')
            sleep(1)
            print('\n                                 Terminating in 2...')
            sleep(1)
            print('\n                                 Terminating in 1...')
            sleep(1)
            quit()

        # If password is incorrect
        else:

            count = count ** 2

            print('Wrong password, the aliens have become', count, 'strong.')
            sleep(2)

            if count > 7600000000:
                print('Earth has been taken over!')
                print('\n\n                                 Lauching nukes, destroying earth in 3...')
                sleep(1)
                print('\n                                 Lauching nukes, destroying earth in 2...')
                sleep(1)
                print('\n                                 Lauching nukes, destroying earth in 1...')

    # Quitting
    if start_quit == 'r':
        os.system('cls')
        print('                                      Good luck out there, hope you do not regret this...')
        sleep(1)
        print('\n\n                                 Terminating in 3...')
        sleep(1)
        print('\n                                 Terminating in 2...')
        sleep(1)
        print('\n                                 Terminating in 1...')
        sleep(1)
        quit()
