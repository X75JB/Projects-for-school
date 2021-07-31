from time import sleep

name = input('State your name:')
print(name.capitalize())
while True:
    print('What would you like to use?')
    print()
    ans = input('[d - diameter or r - radius?]:')
    print()
    if 'd' == ans or 'D' == ans:
        diameter = int(input('Please state your diameter:'))
        print()
        circumference = 3.141 * diameter
        print('Your circumference is', circumference, ' units')
        print()
        print('Would you like to restart?')
        ans2 = input('Yes/no:')
        if 'yes' == ans2 or 'Yes' == ans2:
            break
        elif 'no' == ans2 or 'No' == ans2:
            quit()

    elif 'r' == ans or 'R' == ans:
        radius = int(input('Please state your radius:'))
        circumference = 2 * 3.141 * radius
        print('Your circumference is', circumference, ' units')
        print()
        print('Would you like to restart?')
        ans2 = input('Yes/no:')
        if 'yes' == ans2 or 'Yes' == ans2:
            break
        elif 'no' == ans2 or 'No' == ans2:
            quit()

