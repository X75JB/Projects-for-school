# This program sorts three numbers.
# Jackson Blackman
# 2021_03_23

# Imports

# Title
print('This program sorts numbers.')
print()

# Inputs
while True:
    number_one = int(input('input first number:'))
    number_two = int(input('input second number:'))
    number_three = int(input('input third number:'))

# List
    list = [number_one, number_two, number_three]

# Sorted list
    print(sorted(list))