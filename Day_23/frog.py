# Creating the player turtle object

from turtle import Turtle

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    # Defining turtle movement functions
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.setheading(90)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.setheading(270)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        self.setheading(180)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        self.setheading(0)

    # Reset function if the turtle crosses the road or collides with a car
    def reset(self):
        self.goto(0, -280)