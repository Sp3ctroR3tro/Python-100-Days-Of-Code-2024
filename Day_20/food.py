from turtle import Turtle
import random
# Creating a food class that will inherit all attributes and
# methods from the Turtle class

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # Generate a new random location for the food to populate
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
