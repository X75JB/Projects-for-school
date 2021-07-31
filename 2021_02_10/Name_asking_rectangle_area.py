from time import sleep
name = (input('What is your name:'))
print(name.title())

while True:
    print()
    side = int(input('What is your side value:'))
    print()
    base_one = int(input('What is your base value:'))
    print()
    total = side*base_one
    print(name,',the total area is',total,'Units²')
    print()
    print('Would you like to calculate again?')
    ans = input('Yes/No:')
    if 'yes' == ans or 'Yes' == ans:
        print('restarting')
    if 'no' == ans or 'No' == ans:
        print()
        print('shutting down...')
        sleep(2)
        quit()
