from turtle import *
STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180






class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    # TODO: 1 create a snake body
    # created the first the blocks of snake body
    def create_snake(self):

        for box_pos in STARTING_POS:
            self.add_segment(box_pos)
            
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # TODO: 2 move the snake


    def move(self):
        for seg_num in range(len(self.segments) - 1 ,0 ,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    

    # TODO: 3 control the snake with keypresses


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)             



    # reset snake method added day 24
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(2000,2000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
