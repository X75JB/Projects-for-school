#multiplication chart
#Jackson Blackman
#2021_03_08

from time import sleep

#Starting point
print('This will show you a any multiplication range')
number_multiplied = int(input('Enter the multiplication chart you would like to see:'))
number_length = int(input('What is the largest number that your chart should be multiplied by:'))

#Range generator
max_multiplied = number_length + 1

#Chart generator
for count in range(0, max_multiplied):
    multiplied = number_multiplied * count
    print(number_multiplied,'*',count,'=',multiplied)
