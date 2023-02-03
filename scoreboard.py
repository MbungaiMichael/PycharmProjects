from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 285)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def update(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.clear()
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
        self.penup()
        self.goto(0, 30)
        self.update()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()



