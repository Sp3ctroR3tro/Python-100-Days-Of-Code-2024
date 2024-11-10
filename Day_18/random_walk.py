import turtle
from turtle import Turtle, Screen
import random

# Creating the turtle pointer object
crush = Turtle()
crush.shape("turtle")
crush.color("DarkSeaGreen3", "DarkGoldenrod2")
crush.pensize(15)
turtle.colormode(255)
# color_list = ["DodgerBlue2", "DarkGreen", "DarkSlateGray", "firebrick2", "LawnGreen", "magenta2", "NavajoWhite2", "RoyalBlue2", "goldenrod2", "khaki2"]
crush.speed("fastest")
# Creating the turn angles for the pointer object
angles =  [90, 180, 270, 360]


# Defining a function to generate random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Defining the walk function
def walk():
    for i in range(300):
        crush.color((random_color()))
        crush.forward(30)
        crush.setheading(random.choice(angles))


walk()
screen = Screen()
screen.screensize(2500,2500)
screen.exitonclick()