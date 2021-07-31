import turtle
from time import sleep



#Turtle settings
turtle.Turtle
turtle.Screen()
turtle.pensize(1)
turtle.shape('arrow')
turtle.pencolor('#e7ff00')
turtle.fillcolor('#e7ff00')
turtle.bgcolor('#4a9d9a')
turtle.speed(10)

#Turtle first branch
turtle.forward(100)
turtle.stamp()
turtle.right(180)
turtle.forward(100)

#Turtle for most branches
for x in range(10):

    turtle.right(210)
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(100)

#Turtle for ending branch
turtle.right(210)
turtle.forward(100)
turtle.stamp()
turtle.hideturtle()

#Turtle for exiting
turtle.exitonclick()




