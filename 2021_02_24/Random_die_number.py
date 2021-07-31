#Random dice roller
#Jackson Blackman
#Start /// 2021_02_24 9:43 AM
#End /// 2021_02_24_9:48 AM



import random



print('This is a random dice roll generator')
print()

while True:
    r_q = str(input('Would you like to roll or quit? \n(R/Q):')).lower()
    if r_q == 'r':
        print()
        roll = random.randint(1,6)
        print('You rolled a',roll)
        print()
    elif r_q == 'q':
        quit()
    else:
        print('Error try again')
        print()