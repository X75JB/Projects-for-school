# What should you wear today?
# Jackson Blackman
# 2021-02-23
from time import sleep

while True:
    print('Welcome to what should you wear')
    ans = input('Type "c" for Celsius, "f" for Fahrenheit, "q" to quit (C/N/Q):').lower()
    if ans == 'c':
        celsius = int(input('What is the temperature in Celsius:'))
        if celsius <= 5:
            print('Bundle up, it is cold out there')
            sleep(3)
        elif celsius >= 6 or celsius <= 22:
            print('Wear a sweater, it is chilly')
            sleep(3)
        else:
            print('Wear shorts, it is hot')
            sleep(3)
    elif ans == 'f':
        fahrenheit = int(input('What is the temperature in Celsius:'))
        if fahrenheit <= 41:
            print('Bundle up, it is cold out there')
            sleep(3)
        elif fahrenheit >= 42 or fahrenheit <= 72:
            print('Wear a sweater, it is chilly')
            sleep(3)
        else:
            print('Wear shorts, it is hot')
            sleep(3)
    elif ans == 'q':
        quit()
    else:
        print('ERROR, restarting')
        sleep(2)
