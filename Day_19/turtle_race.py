import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet Prediction", prompt="Enter the color of who you think will win the race:")

# Defining turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Defining the starting positions for turtles
turtles = []
y_positions = [-100, -60, -20, 20, 60, 100, 140]
# Creating a for loop to iterate over the turtle color list and place the turtles in the correct starting position
for index, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)


# Implementing the race logic
start_race = True
while start_race:
    for new_turtle in turtles:
        if new_turtle.xcor() > 230:
            start_race = False
            winning_color = new_turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        move_distance = random.randint(0, 15)
        new_turtle.forward(move_distance)




screen.exitonclick()