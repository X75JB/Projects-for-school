# A mid point calculator
# Jackson Blackman
# 2021_03_22

# Imports

# Title
print('This is a mid-point line calculator')
print('===================================')
print()

# Inputs
while True:
    x_1 = int(input('Please input the value of X1:'))
    y_1 = int(input('Please input the value of Y1:'))
    print()
    x_2 = int(input('Please input the value of X2:'))
    y_2 = int(input('Please input the value of Y2:'))
    print()

# Math and ending product
    x_3 = x_1 + x_2 / 2
    y_3 = y_1 + y_2 / 2
    print('The mid-point of your two coordinates is:',(round(x_3, 2),round(y_3, 2)),)
    print()
    print()
    print()