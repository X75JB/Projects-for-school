# Turtle racing simulator
# Jackson Blackman
# 2021_03_12
# UPDATED ON 2021_03_26

import turtle
import random
from time import sleep

# Variables
race_is_won = False
style = ('Times New Roman', 30)

# Turtles
turtle_one = turtle.Turtle()
turtle_two = turtle.Turtle()
turtle_three = turtle.Turtle()
turtle_four = turtle.Turtle()
turtle_startline = turtle.Turtle()
turtle_title = turtle.Turtle()
turtle_winner = turtle.Turtle()

# Distances for each turtle
turtle_distance_1 = random.randint(1, 5)
turtle_distance_2 = random.randint(1, 5)
turtle_distance_3 = random.randint(1, 5)
turtle_distance_4 = random.randint(1, 5)

# Base options
turtle.Screen()
turtle.bgcolor('#e09d00')

# Title
turtle_title.hideturtle()
turtle_title.up()
turtle_title.setposition(0, -300)
turtle_title.color('black')
turtle_title.write('TURTLE RACE! \n Place your bets!', font=style, align='center')

# Starting line
turtle_startline.hideturtle()
turtle_startline.up()
turtle_startline.speed(1000)
turtle_startline.pensize(4)
turtle_startline.setposition(410, -150)
turtle_startline.down()
turtle_startline.left(90)
turtle_startline.forward(400)

    # Lines down and starting boxes
turtle_startline.left(90)
turtle_startline.forward(850)
turtle_startline.left(90)
turtle_startline.forward(400)
turtle_startline.left(90)
turtle_startline.forward(850)
turtle_startline.left(90)
turtle_startline.forward(100)
turtle_startline.left(90)
turtle_startline.forward(850)
turtle_startline.right(90)
turtle_startline.forward(100)
turtle_startline.right(90)
turtle_startline.forward(850)
turtle_startline.left(90)
turtle_startline.forward(100)
turtle_startline.left(90)
turtle_startline.forward(850)
turtle_startline.right(90)
turtle_startline.forward(100)
turtle_startline.right(90)
turtle_startline.forward(100)
turtle_startline.right(90)
turtle_startline.forward(400)


# Hiding turtles
turtle_one.hideturtle()
turtle_two.hideturtle()
turtle_three.hideturtle()
turtle_four.hideturtle()
turtle_winner.hideturtle()

# Turtle one
turtle_one.up()
turtle_one.shape('turtle')
turtle_one.fillcolor('blue')
turtle_one.setx(-400)
turtle_one.sety(200)
turtle_one.speed(1)

# Turtle two
turtle_two.up()
turtle_two.shape('turtle')
turtle_two.fillcolor('green')
turtle_two.setx(-400)
turtle_two.sety(100)
turtle_two.speed(1)

# Turtle three
turtle_three.up()
turtle_three.shape('turtle')
turtle_three.fillcolor('purple')
turtle_three.setx(-400)
turtle_three.speed(1)

# Turtle four
turtle_four.up()
turtle_four.shape('turtle')
turtle_four.fillcolor('red')
turtle_four.sety(-100)
turtle_four.setx(-400)
turtle_four.speed(1)

# Un-hiding turtles
turtle_one.showturtle()
turtle_two.showturtle()
turtle_three.showturtle()
turtle_four.showturtle()
sleep(3)

# Moving the turtles.
while not race_is_won:
    turtle_one.forward(turtle_distance_1)
    turtle_two.forward(turtle_distance_2)
    turtle_three.forward(turtle_distance_3)
    turtle_four.forward(turtle_distance_4)

# If/elif turtle_X wins

# Turtle_one
    if turtle_one.position()[0] > 400.00:

    # Ends race
        race_is_won = True

    # Clears 'TURTLE RACE! \n Place your bets!'
        turtle_title.clear()

    # Hides other turtles
        turtle_two.hideturtle()
        turtle_three.hideturtle()
        turtle_four.hideturtle()

    # Sets and writes winner text
        turtle_winner.up()
        turtle_winner.hideturtle()
        turtle_winner.setposition(0, 300)
        turtle_winner.color('black')
        turtle_winner.write('Turtle one has won the race', font=style, align='center')

    # Resizes winner turtle
        turtle_startline.clear()
        turtle_one.setposition(0, 0)
        turtle_one.shapesize(3)
        sleep(.1)
        turtle_one.shapesize(7)
        sleep(.1)
        turtle_one.shapesize(10)
        turtle_one.left(90)


# Turtle_two
    elif turtle_two.position()[0] > 400.00:

    # Ends race
        race_is_won = True

    # Clears 'TURTLE RACE! \n Place your bets!'
        turtle_title.clear()

    # Hides other turtles
        turtle_one.hideturtle()
        turtle_three.hideturtle()
        turtle_four.hideturtle()

    # Sets and writes winner text
        turtle_winner.up()
        turtle_winner.hideturtle()
        turtle_winner.setposition(0, 300)
        turtle_winner.color('black')
        turtle_winner.write('Turtle two has won the race', font=style, align='center')

    # Resizes winner turtle
        turtle_startline.clear()
        turtle_two.setposition(0, 0)
        turtle_two.shapesize(3)
        sleep(.1)
        turtle_two.shapesize(7)
        sleep(.1)
        turtle_two.shapesize(10)
        turtle_two.left(90)


# Turtle_three
    elif turtle_three.position()[0] > 400.00:

    # Ends race
        race_is_won = True

    # Clears 'TURTLE RACE! \n Place your bets!'
        turtle_title.clear()

    # Hides other turtles
        turtle_one.hideturtle()
        turtle_two.hideturtle()
        turtle_four.hideturtle()

    # Sets and writes winner text
        turtle_winner.up()
        turtle_winner.hideturtle()
        turtle_winner.setposition(0, 300)
        turtle_winner.color('black')
        turtle_winner.write('Turtle three has won the race', font=style, align='center')

    # Resizes winner turtle
        turtle_startline.clear()
        turtle_three.setposition(0, 0)
        turtle_three.shapesize(3)
        sleep(.1)
        turtle_three.shapesize(7)
        sleep(.1)
        turtle_three.shapesize(10)
        turtle_three.left(90)


# Turtle_four
    elif turtle_four.position()[0] > 400.00:

    # Ends race
        race_is_won = True

    # Clears 'TURTLE RACE! \n Place your bets!'
        turtle_title.clear()

    # Hides other turtles
        turtle_one.hideturtle()
        turtle_two.hideturtle()
        turtle_three.hideturtle()

    # Sets and writes winner text
        turtle_winner.up()
        turtle_winner.hideturtle()
        turtle_winner.setposition(0, 300)
        turtle_winner.color('black')
        turtle_winner.write('Turtle four has won the race', font=style, align='center')

    # Resizes winner turtle
        turtle_startline.clear()
        turtle_four.setposition(0, 0)
        turtle_four.shapesize(3)
        sleep(.1)
        turtle_four.shapesize(7)
        sleep(.1)
        turtle_four.shapesize(10)
        turtle_four.left(90)

# Ends on click
turtle.exitonclick()

