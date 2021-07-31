from math import sqrt
from time import sleep
print("This is a pythagorean theorem calculator")
print()
side_length_one = int(input ("Please put the value of side A here:"))
print()
side_length_two = int(input ("Please put the value of side B here:"))
print()
print(side_length_one, "² +", side_length_two, "² = C²")
print()

side_length_one_total = side_length_one * side_length_one
side_length_two_total = side_length_two * side_length_two

total_one = side_length_one_total + side_length_two_total

print(side_length_one_total, "+", side_length_two_total, "= C²")
print()
print(f'sqrt({total_one}) = C²')
print()

total_two = sqrt(total_one)


print(total_two, "= C")
print()
print("C =", total_two, )
print()
print("The value of side C is", total_two, )
print()
print("side A =", side_length_one, )
print()
print("side B =", side_length_two, )
print()
print("side C =", total_two)

sleep(30)
