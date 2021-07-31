#Even or odd generator
#Jackson Blackman
#2021_02_24



from time import sleep


print('Determines if a number is even or odd')
print()
while True:
    num = int(input('Enter your number:'))
    num2 = num % 2
    if num2 > 0:
        print(num,'is an odd number.')
        print()
        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
        if restart == 'r':
            print()
            print()
            print()
        elif restart == 'q':
            quit()
    else:
        print(num,'is an even number.')
        print()
        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
        if restart == 'r':
            sleep(1)
            print()
            print()
            print()
        elif restart == 'q':
            quit()
