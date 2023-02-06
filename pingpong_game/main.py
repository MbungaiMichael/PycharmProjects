from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.title("Ping pong game")
screen.setup(width=800, height=600)
screen.tracer(0)

tim = Paddle((365, 0))
tim1 = Paddle((-365, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim1.up, "w")
screen.onkey(tim1.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        # ball needs to bounce
        ball.bounce_y()

    # detect collision with paddle and score
    if ball.distance(tim) < 50 and ball.xcor() > 345 or ball.distance(tim1) < 50 and ball.xcor() < -345:
        ball.bounce_x()

    # detect right paddle  misses and score is given to opponent
    if ball.xcor() > 390:
        score.increase_score_1()
        ball.reset_position()

    # detect left paddle misses and score is given to opponent
    if ball.xcor() < -390:
        score.increase_score_2()
        ball.reset_position()

screen.exitonclick()
