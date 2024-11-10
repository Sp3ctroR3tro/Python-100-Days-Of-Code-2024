from turtle import Turtle, Screen
import random

# Creating the turtle pointer object
crush = Turtle()
crush.shape("turtle")
crush.color("DarkSeaGreen3", "DarkGoldenrod2")

#  Making the turtle pointer make a dashed line
# for i in range(50):
#     crush.forward(10)
#     crush.penup()
#     crush.forward(10)
#     crush.pendown()


# Using turtle object to make geometric figures with random colors
color_list = ["DodgerBlue2", "DarkGreen", "DarkSlateGray", "firebrick2", "LawnGreen", "magenta2", "NavajoWhite2", "RoyalBlue2", "goldenrod2", "khaki2"]
keep_drawing = True
while keep_drawing:
    for i in range (3 , 11):
        random_color = random.choice(color_list)
        for j in range(i):
            crush.color(random_color)
            crush.forward(100)
            crush.right(360/i)

    crush.forward(50)
    keep_drawing = False

screen = Screen()
screen.screensize(2500,400)
screen.exitonclick()


