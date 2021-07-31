#This is a number guessing game
#Jackson Blackman
#Start /// 2021_02_24 9:50 AM

import random

count = 0

# Game starting menu:
print('This is a random number guessing game')
start = str(input('Would you like to play this game? \n(Y/N):')).lower()
if start == 'y':

# Difficulty selection:
        while True:
            difficulty = str(input('Please choose your difficulty: \n\nEasy mode:\nFind the random number between 1-250\n\nNormal mode:\nFind the random number between 1-500\n\nHard mode:\nFind the random number between 1-1000\n\nVery hard mode:\n Find the random number between 1-5000\n\nInsanity mode:\nFind the random number between 1-10000\n\nFor easy mode enter "E"\nFor normal mode enter "N"\nFor hard mode enter "H"\nFor very hard mode enter "VH"\nFor insanity mode enter "I"\nWhat mode would you like to play:')).lower()
            print()
            print()
            print()

# Easy mode:
            if difficulty == 'e':
                randomnumber = random.randint(1, 250)
                while True:
                    guess = int(input('Guess a number:'))
                    count = count + 1
                    if guess == randomnumber:
                        print('You have won! Congratulations you guessed it in',count,'tries!')
                        f = open('Number_guessing_game_score.py', 'w')
                        f.write(count)
                        f.close()
                        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
                        if restart == 'r':
                            print()
                            print()
                            print()
                            break

                        elif restart == 'q':
                            quit()
                    elif guess > 250:
                        print()
                        print('Error number not with in range')
                        print()
                    elif guess > randomnumber:
                        print()
                        print('Guess lower')
                        print()
                    elif guess < randomnumber:
                        print()
                        print('Guess higher')
                        print()

# Normal mode:
            elif difficulty == 'n':
                randomnumber = random.randint(1, 500)
                while True:
                    guess = int(input('Guess a number:'))
                    count = count + 1
                    if guess == randomnumber:
                        print('You have won! Congratulations you guessed it in', count, 'tries!')
                        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
                        if restart == 'r':
                            print()
                            print()
                            print()
                            break

                        elif restart == 'q':
                            quit()
                    elif guess > 500:
                        print()
                        print('Error number not with in range')
                        print()
                    elif guess > randomnumber:
                        print()
                        print('Guess lower')
                        print()
                    elif guess < randomnumber:
                        print()
                        print('Guess higher')
                        print()

# Hard mode:
            elif difficulty == 'h':
                randomnumber = random.randint(1, 1000)
                while True:
                    guess = int(input('Guess a number:'))
                    count = count + 1
                    if guess == randomnumber:
                        print('You have won! Congratulations you guessed it in', count, 'tries!')
                        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
                        if restart == 'r':
                            print()
                            print()
                            print()
                            break

                        elif restart == 'q':
                            quit()
                    elif guess > 1000:
                        print()
                        print('Error number not with in range')
                        print()
                    elif guess > randomnumber:
                        print()
                        print('Guess lower')
                        print()
                    elif guess < randomnumber:
                        print()
                        print('Guess higher')
                        print()

# Very hard mode:
            elif difficulty == 'vh':
                randomnumber = random.randint(1, 5000)
                while True:
                    guess = int(input('Guess a number:'))
                    count = count + 1
                    if guess == randomnumber:
                        print('You have won! Congratulations you guessed it in', count, 'tries!')
                        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
                        if restart == 'r':
                            print()
                            print()
                            print()
                            break

                        elif restart == 'q':
                            quit()
                    elif guess > 5000:
                        print()
                        print('Error number not with in range')
                        print()
                    elif guess > randomnumber:
                        print()
                        print('Guess lower')
                        print()
                    elif guess < randomnumber:
                        print()
                        print('Guess higher')
                        print()

# Insane mode:
            elif difficulty == 'i':
                randomnumber = random.randint(1, 10000)
                while True:
                    guess = int(input('Guess a number:'))
                    count = count + 1
                    if guess == randomnumber:
                        print('You have won! Congratulations you guessed it in', count, 'tries!')
                        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
                        if restart == 'r':
                            print()
                            print()
                            print()
                            break

                        elif restart == 'q':
                            quit()
                    elif guess > 10000:
                        print()
                        print('Error number not with in range')
                        print()
                    elif guess > randomnumber:
                        print()
                        print('Guess lower')
                        print()
                    elif guess < randomnumber:
                        print()
                        print('Guess higher')
                        print()
# Ending software
elif start == 'n':
    quit()