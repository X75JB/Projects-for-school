from time import sleep

print('Welcome to the coffee calculator')
print()
coffee = int(input('How many coffees do you have per week?:'))
cost = float(input('How much does one cup of coffee usually cost?:'))
print()
per_day_cost = coffee / 7
per_day_cost_rounded = round(per_day_cost, 2)
per_week_cost = coffee * cost
per_week_cost_rounded = round(per_week_cost, 2)
per_month_cost = per_week_cost * 4
per_month_cost_rounded = round(per_month_cost, 2)
per_year_cost = per_month_cost * 12
per_year_cost_rounded = round(per_year_cost, 2)
per_day_coffee = coffee / 7
per_day_coffee_rounded = round(per_day_coffee, 2)
per_month_coffee = coffee * 4
per_month_coffee_rounded = round(per_month_coffee, 2)
per_year_coffee = per_month_coffee * 12
per_year_coffee_rounded = round(per_year_coffee, 2)
print('Here are your coffee stats: \n\nYour coffee per day: \nCoffee drank per day:',per_day_coffee_rounded,'\nThe amount of money spent on coffee per day:',per_day_cost_rounded,'\n\nYour coffee per week: \nCoffee drank per week',coffee,'\nThe amount of money spent on coffee per week',per_week_cost_rounded,'\n\nYour coffee per month: \nCoffee drank per month',per_month_coffee_rounded,'\nThe amount of money spent on coffee per month',per_month_cost_rounded,'\n\nYour coffee per year: \nCoffee drank per year:',per_year_coffee_rounded,'\nThe amount of money spent on coffee per year:',per_year_cost_rounded)
sleep(30)