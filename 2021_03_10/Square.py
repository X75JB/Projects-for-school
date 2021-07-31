#A coloured square
#Jackson Blackman
#2021_03_10

from time import sleep
import turtle
import random

print('Welcome to my program')
background_color = str(input('Please insert your background colour \nPlease format it in hex code EX:(#49f042)\nHere:'))
fill_color = str(input('Please insert your fill colour \nPlease format it in hex code EX:(#49f042)\nHere:'))
mylist = ['#facb04','#e4f8ce','#975b47','#49f042','#dce121','#dd824c','#ed2bcd','#3af94e']
turtle.Turtle
turtle.hideturtle()
turtle.Screen()
turtle.bgcolor(background_color)
turtle.pencolor('black')
turtle.fillcolor(fill_color)
turtle.speed(3)
turtle.pensize(4)
turtle.begin_fill()
for x in range(4):
    turtle.right(90)
    turtle.forward(100)
turtle.end_fill()
turtle.left(90)
turtle.up()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.down()
turtle.right(90)
for x in range(4):
    turtle.pencolor(random.choice(mylist))
    turtle.forward(200)
    turtle.right(90)
sleep(2)