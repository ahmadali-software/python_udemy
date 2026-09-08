

from turtle import *
from random import *
import colorgram as cg

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
screen.colormode(255)

# extracted_colors = cg.extract("day18/hirst_img.jpg", 30)


# color_list = []
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))

# print(color_list)

color_list = [(200, 165, 112), (236, 239, 244), (146, 78, 54), (55, 94, 123), (163, 152, 49), (218, 201, 145), (135, 162, 182), (136, 32, 22), (51, 119, 87), (194, 94, 76), (71, 44, 38), (18, 97, 70), (163, 144, 157), (106, 75, 79), (232, 176, 166), (142, 175, 156), (145, 20, 25), (35, 60, 77), (183, 204, 175), (84, 146, 127), (71, 37, 40), (34, 67, 96), (169, 100, 103), (16, 71, 57), (221, 177, 180), (104, 126, 154), (36, 82, 87)]
timmy.penup()

# solution 1

# for _ in range(10):
#     for _ in range(10):
#         timmy.dot(20, choice(color_list))
#         timmy.forward(50)
    
#     timmy.setheading(90)
#     timmy.forward(50)
#     timmy.setheading(0)
#     timmy.backward(500)


# solution 2
timmy.speed("fastest")
timmy.hideturtle()


x = -200
current_y = -200
timmy.goto(x,current_y)

for i in range(10):
    for _ in range(10):
        timmy.dot(20, choice(color_list))
        timmy.forward(50)
        # current_x += 50

    # current_x -= 500
    current_y += 50
    timmy.goto(x, current_y)



screen.exitonclick()