# A simple calulator using 'def'
# Jackson Blackman
# 2021_03_23

# Imports

# Title
print('Simple calculator')
print()

# Operation selection
print('Select operation')
while True:
    print()
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print()
    choice = int(input('Enter choice (1/2/3/4):'))

# Number selector
    a = int(input('Enter first number:'))
    b = int(input('Enter second number:'))

# Operation controls
    def add(a, b):
        result = a + b
        return result

    def subract(a, b):
        result = a - b
        return result

    def multiply(a, b):
        result = a * b
        return result

    def divide(a, b):
        result = a / b
        return result

    if choice == 1:
        print(a, '+', b, '=', (add(a, b)))

    if choice == 2:
        print(a, '-', b, '=', (subract(a, b)))

    if choice == 3:
        print(a, '*', b, '=', (multiply(a, b)))

    if choice == 4:
        print(a, '/', b, '=', (divide(a, b)))


