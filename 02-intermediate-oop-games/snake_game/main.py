from turtle import Screen

from score import Score
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.setworldcoordinates(-300, -300, 300, 300)
screen.tracer(0)
game = True
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")

while game:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food) < 15:
        food.food_position()
        score.increase_score()
        snake.grow()
    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        score.game_over()
        snake.reset_snake()
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            snake.reset_snake()
screen.exitonclick()