from turtle import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")

#turning off the tracer to update screen manually 
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# flag 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: 4 detect collision with food :done

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
   # TODO: 6 detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.game_over()
        # game_is_on = False
        scoreboard.reset_board()
        snake.reset_snake()


    # TODO: 7 detect collision with self

    for seg in snake.segments[1:]:
        
        if snake.head.distance(seg) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset_board()
            snake.reset_snake()









screen.exitonclick()