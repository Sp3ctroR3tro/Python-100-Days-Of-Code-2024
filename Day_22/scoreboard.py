from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the scoreboard and redraw both scores."""
        self.clear()  # Clear everything on the screen
        self.goto(-200, 250)  # Move to the left score position
        self.write(self.left_score, align="center", font=("Courier", 24, "normal"))
        self.goto(200, 250)  # Move to the right score position
        self.write(self.right_score, align="center", font=("Courier", 24, "normal"))

    def increase_left_score(self):
        """Increase the left player's score and redraw the scoreboard."""
        self.left_score += 1
        self.update_scoreboard()  # Redraw both scores

    def increase_right_score(self):
        """Increase the right player's score and redraw the scoreboard."""
        self.right_score += 1
        self.update_scoreboard()  # Redraw both scores

    def game_over(self):
        """Display "GAME OVER" in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        if self.left_score > self.right_score:
            self.goto(0, -100)
            self.write("LEFT WINS!", align="center", font=("Courier", 24, "normal"))
        elif self.right_score > self.left_score:
            self.goto(0, -100)
            self.write("RIGHT WINS!", align="center", font=("Courier", 24, "normal"))