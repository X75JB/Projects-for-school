# An income tax calculator
# Jackson Blackman
# 2021_04_08

print('|----------------------------------|')
print('| This is an income tax calculator |')
print('|----------------------------------|')

while True:
    income = int(input('Input income: $'))
    if income < 9999:
        tax = income * .0
        print('You make',income,'with 0% income tax\nYou have to pay $'+str(round(tax, 2)),'in tax.')

    elif income < 19999:
        tax = income * .10
        print('You make',income,'with 10% income tax\nYou have to pay $'+str(round(tax, 2)),'in tax.')

    elif income < 29999:
        tax = income * .25
        print('You make',income,'with 25% income tax\nYou have to pay $'+str(round(tax, 2)),'in tax.')

    elif income < 39999:
        tax = income * .30
        print('You make',income,'with 30% income tax\nYou have to pay $'+str(round(tax, 2)),'in tax.')

    elif income > 40000:
        tax = income * .40
        print('You make',income,'with 40% income tax\nYou have to pay $'+str(round(tax, 2)),'in tax.')

    print()
    print()
    print()
