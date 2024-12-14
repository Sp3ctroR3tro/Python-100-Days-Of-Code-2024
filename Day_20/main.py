from turtle import Turtle, Screen
import random
import time

# Snake body creation function
def create_snake(x_position):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.setx(x_position)
    return snake

# Screen display function
def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen

# Snake forward movement function
def move_snake(snake_segments):
    for i in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[i - 1].xcor()
        new_y = snake_segments[i - 1].ycor()
        snake_segments[i].goto(new_x, new_y)
    snake_segments[0].forward(20)

# Snake basic movement functions
def up():
    # Prevent reversing: Only go up if the snake != moving down (south)
    if snake_head.heading() != 270:
        snake_head.setheading(90)

def down():
    # Prevent reversing: Only go down if the snake != moving up (north)
    if snake_head.heading() != 90:
        snake_head.setheading(270)

def left():
    # Prevent reversing: Only move to the left if the snake != moving to the right (east)
    if snake_head.heading() != 0:
        snake_head.setheading(180)

def right():
    # Prevent reversing: Only move to the right if the snake != moving to the left (west)
    if snake_head.heading() != 180:
        snake_head.setheading(0)





def create_food():
    pass


# Initializing the snake segments
snake_segments = [create_snake(0), create_snake(-20), create_snake(-40)]

snake_head = snake_segments[0]

game_on = True
screen = setup_screen()


# Key bindings for directional movement
screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)


while game_on is True:
    screen.update() # Update the screen once per loop
    time.sleep(0.1) # Control game loop speed
    move_snake(snake_segments) # Calling movement function for snake





screen.exitonclick()


