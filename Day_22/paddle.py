from turtle import Turtle


# Paddle class with movement functions
class Paddle(Turtle):
    def __init__(self, position, max_height=250, min_height=-250):
        super().__init__()
        self.max_height = max_height
        self.min_height = min_height
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y <= self.max_height:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y >= self.min_height:
            self.goto(self.xcor(), new_y)