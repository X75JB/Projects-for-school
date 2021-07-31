# A box drawing
# Jackson Blackman
# 2021_03_23

# Imports
import turtle
import random


# Colours
mylist = ['#facb04',
          '#e4f8ce',
          '#975b47',
          '#49f042',
          '#dce121',
          '#dd824c',
          '#ed2bcd',
          '#3af94e',
          '#fa852e',
          '#1853e2',
          '#38a483',
          '#fe4974',
          '#c40d70',
          '#853b05',
          '#4e2967',
          '#e7aa91',
          '#2be0ad',
          '#cf0328',
          '#1f3a2a',
          '#0e1313',
          '#b8371b']

# Turtle settings
turtle.Turtle
turtle.hideturtle()
turtle.Screen()
turtle.bgcolor('white')
turtle.pencolor('black')
turtle.fillcolor('white')
turtle.speed(3)
turtle.pensize(4)

# Moving turtle into place
turtle.up()
turtle.goto(0,0)
turtle.down()

# First 4-box set 'def'
def square_1():
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.left(-90)

# Square set one being created
for x in range(4):
    square_1()

# Rotating boxes
turtle.left(45)

# Second 4-box set 'def'
def square_2():
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
    turtle.left(-90)

# Square set two being created
for x in range(4):
    square_2()

# Exit on click
turtle.exitonclick()