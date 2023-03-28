from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_is_on = True

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_point()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 282 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
