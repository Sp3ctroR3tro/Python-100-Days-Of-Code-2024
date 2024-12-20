from turtle import Turtle


class Snake:
    def __init__(self):
        # Initialize the snake with three body segments
        self.snake_segments = [self.create_snake(0), self.create_snake(-20), self.create_snake(-40)]
        self.head = self.snake_segments[0]

    def create_snake(self, x_position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.setx(x_position)
        return snake

    # Extending the snake if food is hit
    def extend(self):
        self.snake_segments.append(self.create_snake(self.snake_segments[-1].xcor()))


    # Snake forward movement function
    def move_snake(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        #     pixels that snake will move
        self.snake_segments[0].forward(15)

    # Snake basic movement functions
    def up(self):
        # Prevent reversing: Only go up if the snake != moving down (south)
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        # Prevent reversing: Only go down if the snake != moving up (north)
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        # Prevent reversing: Only move to the left if the snake != moving to the right (east)
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # Prevent reversing: Only move to the right if the snake != moving to the left (west)
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        # Remove all current segments from the screen
        for segment in self.snake_segments:
            segment.goto(1000, 1000)  # Move the segment out of the visible screen
        self.snake_segments.clear()  # Clear the list of segments

        # Recreate the snake starting position
        self.snake_segments = [self.create_snake(0), self.create_snake(-20), self.create_snake(-40)]
        self.head = self.snake_segments[0]