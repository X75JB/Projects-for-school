from math import sqrt
from time import sleep

while True:
    while True:
        print("What do you want to calculate!")
        number = float(input('First Number:'))
        number_2 = float(input('Second Number:'))
        print('What operation do you want to use? [x - Multiply, / - Divide, close]')
        ans = input('Operation:')
        if 'x' == ans or 'X' == ans:
            answer = (number * number_2)
            print(f'{number} x {number_2} = {number * number_2}')
        elif '/' == ans:
            print(f'{number} / {number_2} = {number / number_2}')
        elif 'close' == ans or 'Close' == ans:
            print('closing application...')
            sleep(3)
            quit()
        else:
            print('ERROR 1: not a valid operation')
            sleep(3)
            print('closing application...')
            sleep(3)
            quit()

        print('Would you like to further the question?')
        ans2 = input('Yes/close:')
        if 'yes' in ans2:
            print('Choose from the list [s - Squareroot, x - Multiply, / - Divide, r - restart]')
            ans3 = input('Operation:')
            if 's' == ans3 or 'S' == ans3:
                print(f'sqrt(,answer,)')
            elif 'x' == ans3 or 'X' == ans3:
                print(f'{number} x {number_2} = {number * number_2}')
            elif '/' == ans3:
                print(f'{number} / {number_2} = {number / number_2}')
            elif 'r' == ans3 or 'R' == ans3:
                break

        if 'close' == ans2 or 'Close' == ans2:
            print('closing application...')
            sleep(3)
            quit()

        print('Would you like to calculate again?')
        ans4 = input('Yes/No:')
        if 'yes' != ans4 and 'Yes' != ans4:
            break
        if 'no' == ans4 or 'No' == ans4:
                quit()


