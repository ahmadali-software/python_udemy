
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height= 600)
screen.title("pong")

screen.tracer(0)
screen.listen()

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()





screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



global is_game_on 
is_game_on = True

# created this function to stop the gmae when user clicks q  
def game_over():
    global is_game_on
    is_game_on = False
    # screen.bye()


while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 3 detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 4: detect collision with between padle and ball and change the dirction of ball after collison 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 5: if ball goes out off boundiries of game other player gets a point and ball resets 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        
        

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()       
        scoreboard.update_scoreboard()

    
    screen.onkey(game_over, "q")

screen.exitonclick()
