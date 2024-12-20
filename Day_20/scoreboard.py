from turtle import Turtle

# Creating a scoreboard class that will inherit
# all attributes and methods from the Turtle class

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()


    # Update the scoreboard with the current score and the highscore
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))


    # Reset the score at the start of each new run
    def reset(self):
        self.score = 0
        self.update_scoreboard()

    # Increase the score each time the snake touches food
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    # Creating the game over function
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
