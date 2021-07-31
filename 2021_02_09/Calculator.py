

while True:
    print("What do you want to calculate!")
    number = float(input('First Number:'))
    number_2 = float(input('Second Number:'))
    print('What operation do you want to use? [x - Mutlipy, / - Divide]')
    ans = input('Operation:')
    if 'x' in ans:
        print(f'{number} x {number_2} = {number * number_2}')
    elif '/' in ans:
        print(f'{number} / {number_2} = {number / number_2}')
    else:
        print('That is not a valid option')


