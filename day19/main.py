from turtle import *

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)


def move_backwards():
    
    timmy.backward(10)

def move_right():
    timmy.setheading(timmy.heading() + 5) 
    # timmy.forward(10)

def move_left():
    timmy.setheading(timmy.heading() - 5) 
    # timmy.forward(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.goto(0,0)
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()