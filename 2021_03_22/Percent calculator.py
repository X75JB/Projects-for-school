# A percent calculator for tests
# Jackson Blackman
# 2021_03_22

# Imports
from time import sleep

# Titles
print('This program calculates test percentages')
print('========================================')
print()

# Inputs
while True:
    total = int(input('What is the overall mark of the test:'))
    earned = int(input('What is the mark you recived on the test:'))

# Math
    mark = earned / total * 100

# Error system
    if total < earned:
        print('ERROR not a valid range, please restart')
        sleep(5)
        break

# End product
    print(earned,'out of',total,'is',str(round(mark, 1)) + '%')
    print()
