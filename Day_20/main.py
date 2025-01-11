# Importing needed modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen display function
def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = setup_screen()

# Key bindings for directional movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on is True:
    screen.update() # Update the screen once per loop
    time.sleep(0.1) # Control game loop speed
    snake.move_snake() # Calling movement function for snake


    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        food.check_collision(snake)
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()



screen.exitonclick()