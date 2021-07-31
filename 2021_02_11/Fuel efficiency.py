from time import sleep


print('This calculates trip cost')
print()
while True:
    car = input('State your car make and model:')
    fuel_efficiency = float(input('State the amount of fuel you use per 100 km:'))
    km = float(input('State the amount of km you will be driving:'))
    fuel_cost = float(input('State the cost of fuel per liter:'))
    print()
    fuel_used = km / fuel_efficiency
    rounded_fuel_used = round(fuel_used,2)
    money_spent = fuel_used * fuel_cost
    rounded_money_spent = round(money_spent,2)
    print('Your',car,'has used',rounded_fuel_used,'liters of fuel on this trip.\nThis trip has cost you',rounded_money_spent,'$')
    print()
    sleep(2)
