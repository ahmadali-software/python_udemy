import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()



screen.listen()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkey(player.move, "Up")
    carmanager.create_car()
    carmanager.move_car()

    # Detect collision between cars and turtle
    for car in carmanager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect turtle reaching finish line
    if player.is_at_finish_line():
        player.reset_pos()
        carmanager.increase_car_speed()
        scoreboard.increace_level()

screen.exitonclick()    
