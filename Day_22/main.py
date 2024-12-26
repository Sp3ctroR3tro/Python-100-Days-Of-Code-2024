# Importing needed modules
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Initializing the screen
def setup_screen():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    return screen

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_screen = setup_screen()


# Key binding to move the user paddle
game_screen.listen()
keys = {"w": False, "s": False, "Up": False, "Down": False}
def key_press(key):
    keys[key] = True
def key_release(key):
    keys[key] = False
game_screen.onkeypress(lambda: key_press("w"), "w")
game_screen.onkeyrelease(lambda: key_release("w"), "w")
game_screen.onkeypress(lambda: key_press("s"), "s")
game_screen.onkeyrelease(lambda: key_release("s"), "s")
game_screen.onkeypress(lambda: key_press("Up"), "Up")
game_screen.onkeyrelease(lambda: key_release("Up"), "Up")
game_screen.onkeypress(lambda: key_press("Down"), "Down")
game_screen.onkeyrelease(lambda: key_release("Down"), "Down")

game_on = True

while game_on:
    time.sleep(0.016)
    if keys["w"]:
        left_paddle.go_up()
    if keys["s"]:
        left_paddle.go_down()
    if keys["Up"]:
        right_paddle.go_up()
    if keys["Down"]:
        right_paddle.go_down()

    # Move the ball once the game has started
    ball.move()

    # Detect top or bottom wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting paddle collisions
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect if right user scores
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.increase_right_score()

    # Detect if left user scores
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.increase_left_score()


    # Detect winner
    if scoreboard.left_score == 11:
        game_on = False
        scoreboard.game_over()
    if scoreboard.right_score == 11:
        game_on = False
        scoreboard.game_over()

    game_screen.update()








game_screen.exitonclick()
