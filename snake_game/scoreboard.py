from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 285)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update()



