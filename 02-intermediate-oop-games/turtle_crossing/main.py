from turtle import Screen
import player
from player import Player
from cars import Car
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()
screen.onkey(turtle.move, "w")
score = Score()
score.current_level()
cars = Car()
MIN_DISTANCE = 30
game = True
while game:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.car_move()
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game = False
            score.game_over()
    if turtle.ycor() > 270:
        turtle.goto(player.STARTING_POSITION)
        score.level_up()
        cars.reset_cars()
        cars.accelerate()
screen.exitonclick()