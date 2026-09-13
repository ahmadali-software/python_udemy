from turtle import Turtle

# TODO: 5 create a scoreboard: done


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        # added day 24
        
        with open("day20+21/highscorefile.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        # self.write(f"score: {self.score}", align= "center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()


        

    def update_scoreboard(self):
        
        self.clear()
        
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align= "center", font=("Arial", 24, "normal"))


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align= "center", font=("Arial", 24, "normal"))

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("day20+21/highscorefile.txt", mode='w') as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
