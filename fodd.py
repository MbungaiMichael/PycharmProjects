from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        random_int_x = random.randint(-300, 300)
        random_int = random.randint(-300, 300)
        self.goto(random_int_x, random_int)
        