#AmrMualla Snake Game w/ Python Turtle Graphics and OOP
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Amr's Snake Game")
screen.tracer(0)
starting_pos = [(0,0), (-20, 0), (-40,0)]

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")

game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for part in snake.parts:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()


