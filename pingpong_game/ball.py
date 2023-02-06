from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('purple')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.y_cor = 10
        self.x_cor = 10

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_cor *= -1

    def bounce_x(self):
        self.x_cor *= -1

    def reset_position(self):
        self.goto(0, 0)
