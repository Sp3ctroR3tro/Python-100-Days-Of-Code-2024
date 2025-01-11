from turtle import Turtle
import os

# Creating a scoreboard class that will inherit
# all attributes and methods from the Turtle class

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.load_highscore()
        self.update_scoreboard()


    # Update the scoreboard with the current score and the highscore
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}", align="center", font=("Courier", 24, "normal"))


    # Reset the score at the start of each new run
    def reset(self):
        self.score = 0
        self.update_scoreboard()

    # Increase the score each time the snake touches food
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # Increase the highscore each time the user score beats the highscore
    def increase_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.update_scoreboard()

    # Creating a highscore write file
    def write_highscore(self):
        try:
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(str(self.highscore))
        except Exception as e:
            print(f"Error writing highscore: {e}")

    # Load the highscore
    def load_highscore(self):
        try:
            # Look to see if there is a highscore file within the current folder
            if os.path.exists("highscore.txt"):
                with open("highscore.txt", mode="r") as highscore:
                    self.highscore = int(highscore.read())
            else:
                self.write_highscore()
        except Exception as e:
            print(f"Error loading highscore: {e}")


    # Creating the game over function
    def game_over(self):
        self.increase_highscore()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
