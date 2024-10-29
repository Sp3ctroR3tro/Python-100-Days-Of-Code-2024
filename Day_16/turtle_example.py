from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkSeaGreen3", "DarkGoldenrod2")

for i in range(4):
# Making Timmy the turtle move
    timmy.forward(100)
    # Left and right turns are handled in degrees
    timmy.left(90)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()