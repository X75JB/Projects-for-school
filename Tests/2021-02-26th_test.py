#This is a Tip Calculator
#Jackson Blackman
#2021-02-26

from time import sleep

print('                                     ----------------------')
print('                                     |   Tip Calculator   |')
print('                                     ----------------------')
print()
name = str(input('What is your name:')).capitalize()
name_server = str(input('What is the name of your server:')).capitalize()
restaurant = str(input('What restaurant are you eating at:')).capitalize()
food_cost = float(input('What is the food cost before tax: $'))
food_cost_tax = food_cost * 1.13
print('The food cost including tax is $',round(food_cost_tax, 2))
print()
print('Quality of Service')
print('------------------')
print()
print('For the next question, choose between "terrible", "okay", "good", or "great"')
print()
service = str(input('How was the service:')).lower()
tip = (input('What percentage of tip will you give (0, 10, 15, or 20):'))
if tip == '0':
    print()
    print('Your total bill is',food_cost_tax)
    print()
    print(name_server + ', because the service at', restaurant + ' was', service + ', my tip is', tip + '%.\nThanks,',name + '! Please come again!')
    sleep(120)

elif tip == '10':
    print()
    print('Your total bill is',round(food_cost_tax * 1.10,2))
    print()
    print(name_server + ', because the service at', restaurant + ' was', service + ', my tip is', tip + '%.\nThanks,',name + '! Please come again!')
    sleep(120)

elif tip == '15':
    print()
    print('Your total bill is',round(food_cost_tax * 1.15, 2))
    print()
    print(name_server + ', because the service at', restaurant + ' was', service + ', my tip is', tip + '%.\nThanks,',name + '! Please come again!')
    sleep(120)

elif tip == '20':
    print()
    print('Your total bill is',round(food_cost_tax * 1.20,2))
    print()
    print(name_server + ', because the service at', restaurant + ' was', service + ', my tip is',tip + '%.\nThanks,', name + '! Please come again!')
    sleep(120)