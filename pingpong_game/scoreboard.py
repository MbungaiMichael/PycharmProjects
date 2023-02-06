from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f" Score: {self.score_1} : {self.score_2}", align="center", font=('Arial', 15, 'normal'))
        self.hideturtle()

    def update(self):
        self.write(f"self : {self.score_1}:{self.score_2}", align="center", font=('Arial', 15, 'normal'))

    def increase_score_1(self):
        self.score_1 += 1
        self.clear()
        self.update()

    def increase_score_2(self):
        self.score_2 += 1
        self.clear()
        self.update()
