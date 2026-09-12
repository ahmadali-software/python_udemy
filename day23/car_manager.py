COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# TODO 2:  create cars randomly, moving across the y-axis by 10 steps

from turtle import Turtle
from random import randint, choice

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

        
        

    def create_car(self):

        # random chance reduce the number of cars
        random_chance = randint(1,6)
        if random_chance == 1 or random_chance == 4:

            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250, 250))
            self.cars.append(new_car)
            
        


    def move_car(self):
        
           for car in self.cars:
                car.backward(self.car_speed)


    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

    
