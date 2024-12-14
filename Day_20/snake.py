from turtle import Turtle


class Snake:
    def __init__(self):
        # Initialize the snake with three body segments
        self.snake_segments = [self.create_snake(0), self.create_snake(-20), self.create_snake(-40)]
        self.snake_head = self.snake_segments[0]

    def create_snake(self, x_position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.setx(x_position)
        return snake

    # Snake forward movement function
    def move_snake(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        #     pixels that snake will move
        self.snake_segments[0].forward(20)

    # Snake basic movement functions
    def up(self):
        # Prevent reversing: Only go up if the snake != moving down (south)
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        # Prevent reversing: Only go down if the snake != moving up (north)
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        # Prevent reversing: Only move to the left if the snake != moving to the right (east)
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        # Prevent reversing: Only move to the right if the snake != moving to the left (west)
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)