from turtle import Screen
import time
from frog import Frog
from cars import CarManager
from scoreboard import Scoreboard

# Initializing the screen
def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Turtle Crossing")
    screen.tracer(0)
    return screen

frog = Frog()
car_manager = CarManager()
game_screen = setup_screen()
scoreboard = Scoreboard()

# Key bindings
game_screen.listen()
game_screen.onkey(frog.go_up, "Up")
game_screen.onkey(frog.go_down, "Down")
game_screen.onkey(frog.go_left, "Left")
game_screen.onkey(frog.go_right, "Right")

# Main game loop
game_start = True
previous_y = frog.ycor()
while game_start:
    # Control game speed to 60 FPS
    time.sleep(0.016)

    # Spawn cars
    car_manager.spawn_cars()
    car_manager.move_cars()

    # Score progression
    if frog.ycor() > previous_y:
        # Increase the users score by 100 each time they make it to the next lane
        scoreboard.increase_score(100)
        previous_y = frog.ycor()

    # Level progression
    if frog.ycor() > 280:
        frog.reset()
        car_manager.increase_speed()
        # Increase the users score by 1000 each time they advance to the next level
        scoreboard.increase_score(1000)
        scoreboard.increase_level()
        previous_y = frog.ycor()

    # Car collision detection
    for car in car_manager.all_cars:
        if car.distance(frog) < 20:
            game_start = False
            scoreboard.game_over()



    game_screen.update()

game_screen.exitonclick()