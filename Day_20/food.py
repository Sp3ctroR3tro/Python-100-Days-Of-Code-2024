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

    # Check to see if the snakes body on top of the food spawn point
    def check_collision(self, snake):
        for segment in snake.snake_segments:
            if self.distance(segment) < 20:
                self.refresh()
                self.check_collision(snake)