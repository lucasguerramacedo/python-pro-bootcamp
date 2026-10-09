from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
GOAL_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)