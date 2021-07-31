#Overall area calculator
#Jackson Blackman
#2021-02-23
from time import sleep



while True:
    print('This is an area calculator')
    ans = input('What would you like to calculate? \ns for area of a square \nt for area of a triangle \nc for area of a circle \n(S/T/C):').lower()
    print()
    if ans == 's':
        ans2 = int(input('What is the side length of your square?:'))
        square_area = ans2*ans2
        print('The area of your square is',square_area,'units')
        print()
        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
        if restart == 'r':
            sleep(1)
            print()
            print()
            print()
        elif restart == 'q':
            quit()
    elif ans == 't':
        base = int(input('What is the base length of the triangle?:'))
        print()
        height = int(input('What is the height length of the triangle?:'))
        triangle_area = base*height/2
        print('The area of your triangle is',triangle_area,'units')
        print()
        restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
        if restart == 'r':
            sleep(1)
            print()
            print()
            print()
        elif restart == 'q':
            quit()

    elif ans == 'c':
        print('What would you like to use?')
        ans4 = input('Would you like to use diameter or radius? \n(D/R):')
        if 'd' == ans4 or 'D' == ans4:
            diameter = int(input('Please state your diameter:'))
            print()
            circumference = 3.141 * diameter
            print('Your circumference is', circumference, ' units')
            print()
            restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
            if restart == 'r':
                sleep(1)
                print()
                print()
                print()
            elif restart == 'q':
                quit()

        elif 'r' == ans4 or 'R' == ans4:
            radius = int(input('Please state your radius:'))
            circumference = 2 * 3.141 * radius
            print('Your circumference is', circumference, ' units')
            print()
            restart = str(input('Would you like to restart or quit?(R/Q)')).lower()
            if restart == 'r':
                sleep(1)
                print()
                print()
                print()
            elif restart == 'q':
                quit()
