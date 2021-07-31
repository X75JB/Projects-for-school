from time import sleep

name = input('Please state your name:')
while True:
    print('Converts fahrenheit to celsius')
    print()
    print(name.capitalize())
    print()
    degrees = int(input('What is your degrees in fahrenheit:'))
    celsius = degrees - 32 * 5 / 9
    round(celsius, 2)
    print('Your temperature is', celsius, 'celsius or', degrees, 'fahrenheit')
    sleep(2)
