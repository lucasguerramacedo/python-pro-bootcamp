from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from score import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setworldcoordinates(-400, -300, 400, 300)
paddle1 = Paddle()
paddle1.goto(350, 0)
paddle2= Paddle()
paddle2.goto(-350,0)
ball = Ball()
score = Score()
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


game = True
while game:
    time.sleep(ball.acceleration)
    screen.update()
    ball.move()
    if -300 < ball.xcor() < 300:
        ball.can_bounce = True
    if abs(ball.ycor()) > 300:
        ball.wall_bounce()
    if ball.xcor() > 320 and ball.distance(paddle1) < 50 and ball.can_bounce:
        ball.paddle_bounce()
        ball.can_bounce = False
    if ball.xcor() < -320 and ball.distance(paddle2) < 50 and ball.can_bounce:
        ball.paddle_bounce()
        ball.can_bounce = False
    if ball.xcor()  > 430:
        score.l_point()
        ball.reset()
    if ball.xcor() < -430:
        score.r_point()
        ball.reset()

screen.exitonclick()
