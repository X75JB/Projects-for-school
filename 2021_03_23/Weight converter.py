# Calculates how much weight you have lost
# Jackson Blackman
# 2021_03_23

# Imports

# Title
print()
print('This program calculates the % of fat you have lost')

# Inputs
while True:
    p_kg = str(input('Kg or Pounds:')).lower()
    starting_weight = int(input('Starting weight:'))
    current_weight = int(input('Current weight:'))

# Math
    weight_lost = starting_weight - current_weight
    weight_lost_percent = weight_lost / starting_weight * 100

# End products
    print('You have lost', round(weight_lost, 2), p_kg)
    print('You have lost', str(round(weight_lost_percent, 2)) + '% of your body weight')
    print()
