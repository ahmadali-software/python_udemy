FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-270,250)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font= FONT)

    def increace_level(self):
        self.level +=1
        self.write_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center" ,font= FONT)