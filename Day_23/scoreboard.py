from turtle import Turtle


# Creating a scoreboard class that displays current user score and level
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} Score: {self.score}", align="left", font=("Courier", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

