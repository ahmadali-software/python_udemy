from turtle import *
from random import *

timmy = Turtle()

timmy.shape("turtle")
timmy.color("blue4")
screen = Screen()
screen.colormode(255)

# drwaing a squire
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# dashed line
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# different shapes 

# def draw_shapes(num_of_sides):
#     angle = 360/num_of_sides

#     for i in range(num_of_sides):
        
#         timmy.forward(100)
#         timmy.right(angle)


# for i in range(3, 10):
#     timmy.pencolor(randint(0,255), randint(0,255), randint(0,255))
#     draw_shapes(i)


# random walk



#  my attempt

# timmy.pensize(15)
# for i in range(100):
#     timmy.pencolor(randint(0,255), randint(0,255), randint(0,255))
#     move = randint(1,3)
#     if move == 1:
#         timmy.forward(20)

#     elif move == 2:
#         timmy.right(90)
#         timmy.forward(20)
#     else:
#         timmy.left(90)
#         timmy.forward(20)


# another solution:

dirctions = [0, 90, 180, 270]
timmy.pensize(10)
for i in range(100):
    timmy.pencolor(randint(0,255), randint(0,255), randint(0,255))
    timmy.setheading(choice(dirctions))
    timmy.forward(30)


screen.exitonclick()
