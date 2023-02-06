from turtle import Turtle
POSI = [(0, 0), (-20, 0), (-40, 0)]
Move_DIS = 20


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segmens = []
        self.appear()
        self.head = self.segmens[0]

    def appear(self):
        for position in POSI:
            self.add_segmens(position)


    def add_segmens(self, position):
        scn1 = Turtle('square')
        scn1.color("white")
        scn1.penup()
        scn1.goto(position)
        self.segmens.append(scn1)

    def extend(self):
        self.add_segmens(self.segmens[-1].position())

    def move(self):
        for seg_num in range(len(self.segmens) - 1, 0, -1):
            new_x = self.segmens[seg_num - 1].xcor()
            new_y = self.segmens[seg_num - 1].ycor()
            self.segmens[seg_num].goto(new_x, new_y)
        self.head.fd(Move_DIS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def rights(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def lefts(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def reset(self):
        for seg in self.segmens:
            seg.goto(1000, 1000)
        self.segmens.clear()
        self.appear()
        self.head = self.segmens[0]
