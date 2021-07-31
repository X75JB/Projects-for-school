# A program that shows you the amount of days in a month
# Jackson Blackman
# 2021_03_26

# Imports.

# Title.
print('====================================================')
print('|This program outputs the number of days in a month|')
print('====================================================')
print()

# While true loop asking for the month.
while True:
    month_name = str(input('Month:')).lower()

# Months with 28 or 29 days (February).
    if month_name == 'february':
        print('February has 28/29 days.')
        print()

# Months with 30 days (April, June, September, November).
    elif month_name == 'april' or month_name == 'june' or month_name == 'september' or month_name == 'november':
        print((month_name).capitalize(), 'has 30 days.')
        print()

# Months with 31 days (January, March, May, July, August, October, December).
    elif month_name == 'january' or month_name == 'march' or month_name == 'may' or month_name == 'july' or month_name == 'august' or month_name == 'october' or month_name == 'december':
        print((month_name).capitalize(), 'has 31 days.')
        print()

# Error system for spelling or incorrect name.
    else:
        print('Error not a valid month, check spelling.')
        print()
