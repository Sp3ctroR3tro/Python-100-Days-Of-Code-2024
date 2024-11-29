from turtle import Turtle, Screen

cursor = Turtle()


def move_forward():
    cursor.forward(10)
def move_backward():
    cursor.backward(10)
def move_left():
    cursor.left(10)
def move_right():
    cursor.right(10)
def clear():
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()