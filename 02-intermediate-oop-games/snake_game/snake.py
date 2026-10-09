from turtle import Turtle, Screen
MOVE_DISTANCE = 20
POSITIONS = (0, 0), (-20, 0), (-40, 0)
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.direction_locked = False
    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)
    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
        self.direction_locked = False

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color("green")
        new_segment.penup()
        new_segment.shape("square")
        new_segment.setpos(position)
        self.segment.append(new_segment)

    def grow(self):
        self.add_segment(self.segment[-1].position())
    def snake_move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            self.segment[seg_num].goto(self.segment[seg_num-1].pos())
        self.head.forward(MOVE_DISTANCE)
        self.direction_locked = False
    def right(self):
        if self.head.heading() != 180 and not self.direction_locked:
            self.head.setheading(0)
            self.direction_locked = True
    def left(self):
        if self.head.heading() != 0 and not self.direction_locked:
            self.head.setheading(180)
            self.direction_locked = True
    def up(self):
        if self.head.heading() != 270 and not self.direction_locked:
            self.head.setheading(90)
            self.direction_locked = True
    def down(self):
        if self.head.heading() != 90 and not self.direction_locked:
            self.head.setheading(270)
            self.direction_locked = True