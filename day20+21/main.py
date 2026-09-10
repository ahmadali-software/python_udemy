from turtle import *
from snake import Snake
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")

#turning off the tracer to update screen manually 
screen.tracer(0)

snake = Snake()

# flag 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")






# TODO: 4 detect collision with food


# TODO: 5 create a scoreboard


# TODO: 6 detect collision with wall

# TODO: 7 detect collision with self



screen.exitonclick()