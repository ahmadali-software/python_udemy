from turtle import *
import random


screen = Screen()
screen.setup(width=500, height=400)

# flag for race
is_race_on = False


# getting user guess
user_bet = screen.textinput(title="make your bid", prompt="which color will win the reace?")

# creating list of colors which i used to loop through turtles 
colors = ["red", "green", "blue", "purple", "orange", "yellow"]

# list of turtle objects
turtles = []


yPos = -100

# creating turtles in starting pos
for element in colors:

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(element)

    turtles.append(new_turtle)


    new_turtle.goto(x=-225, y=yPos)
    yPos+=30


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtles:
        # check if any turtle crossed finish line
        if turtle.xcor() > 220:
            is_race_on = False
            # comparing guess with winner
            if turtle.pencolor() == user_bet:
                print("great guess you won")
            else:
                print(f"wrong guess, {turtle.pencolor()} won ")
            
        # random movment 
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
         
     


screen.exitonclick()