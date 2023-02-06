from turtle import Screen
import time
from snake import Snake
from fodd import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)

# creates a snake
snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.lefts, "Left")
screen.onkey(snake.rights,  "Right")

# snake moves
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with the food

    if snake.head.distance(food) < 14:
        score.increase_score()
        snake.extend()
        food.refresh()

    # detect collision with the wall

    if snake.head.xcor() > 325 or snake.head.xcor() < -320 or snake.head.ycor() > 325 or snake.head.ycor() < -320:
        score.reset()
        snake.reset()

    # detect collision with the snake body
    for segmen in snake.segmens[1:]:
        if snake.head.distance(segmen) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
 