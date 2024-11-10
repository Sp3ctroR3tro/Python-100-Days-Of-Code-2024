import turtle
from turtle import Turtle, Screen

# import colorgram
#
# Extracting 50 colors from the image
# image_colors = colorgram.extract(
#     'hq720.jpg',50)
#
# Creating a list and adding the RGB tuples to the list
# rgb_list = []
# for rgb in image_colors:
#     rgb_list.append((rgb.rgb.r, rgb.rgb.g, rgb.rgb.b))
#
# Viewing the list.
# print(rgb_list)


# Setting the dot colors for the Hirst painting
color_list = [(189, 161, 124), (192, 167, 177), (166, 84, 43), (201, 186, 192), (40, 110, 157), (127, 164, 191), (157, 61, 94), (205, 214, 229), (195, 84, 114), (148, 149, 58), (43, 127, 69), (210, 202, 145), (132, 177, 159), (159, 18, 48), (203, 221, 209), (20, 45, 135), (74, 9, 44), (213, 181, 177), (13, 13, 79), (69, 166, 136), (201, 91, 74), (167, 22, 14), (52, 156, 180), (76, 23, 10), (16, 100, 54), (104, 120, 172), (12, 57, 21), (170, 205, 185), (180, 184, 215), (164, 203, 211), (11, 93, 106), (78, 82, 29)]
turtle.colormode(255)

# Setting the starting position of the turtle pointer for the Hirst painting.
crusher = Turtle()
crusher.speed("fastest")
crusher.setheading(225)
crusher.penup()
crusher.hideturtle()
crusher.forward(500)
crusher.setheading(0)
crusher.pendown()

def hirst_paint(dot_number):
    for i in range(dot_number):
        crusher.dot(20,color_list[i % len(color_list)])
        crusher.setheading(0)
        crusher.penup()
        crusher.forward(50)
        if (i + 1) % 10 == 0:
            crusher.setheading(90)
            crusher.forward(50)
            crusher.setheading(180)
            crusher.forward(500)
            crusher.setheading(0)




hirst_paint(100)



screen = Screen()
screen.screensize(1000,1000)
screen.exitonclick()