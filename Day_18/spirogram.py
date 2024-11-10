import turtle
from turtle import Turtle, Screen
import random


# Creating the turtle pointer object
crush = Turtle()
crush.shape("turtle")
crush.color("DarkSeaGreen3", "DarkGoldenrod2")
turtle.colormode(255)
crush.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spiral(gap_size):
    for i in range(int(360/gap_size)):
        crush.circle(100)
        crush.color(random_color())
        crush.setheading(crush.heading() + gap_size)


spiral(5)



screen = Screen()
screen.screensize(2500,400)
screen.exitonclick()

