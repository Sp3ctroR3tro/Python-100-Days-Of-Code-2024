from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 5
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        # Change car shape
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        # Spawn cars on the right edge of the map 
        self.goto(300, random.randint(-250, 250))
        self.color(random.choice(colors))
        # Make cars move towards the left side of the screen
        self.setheading(180)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())


class CarManager:
    def __init__(self):
        # Initialize a car manager.
        self.all_cars = []  # List to hold all car instances
        self.speed = STARTING_MOVE_DISTANCE

    def spawn_cars(self):
        # Create new cars at random intervals.
        # Randomly create a car (e.g., on 1/6 chance per game tick)
        if random.randint(1, 15) == 1:  # Adjust ratio for car frequency
            new_car = Car()
            self.all_cars.append(new_car)

    def move_cars(self):
        # Move all cars leftwards.
        for car in self.all_cars:
            car.move()

    def increase_speed(self):
        # Increase car speed to make the game harder.
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT