#Should you use an umbrella?
#Jackson Blackman
#2021-02-23
from time import sleep



print('Welcome to should you use an umbrella?')
ans = input('Is it raining? (Y/N):')
if ans == 'Y' or ans == 'y':
    print('Today you should bring an umbrella')
    sleep(3)
    quit()
elif ans == 'N' or ans == 'n':
    print('Today you do not need to bring an umbrella')
    sleep(3)
    quit()