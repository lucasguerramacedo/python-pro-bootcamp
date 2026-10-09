from turtle import Turtle
FONT = ("courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.goto(-280, 250)
    def current_level(self):
        self.write(f"Level {self.level}", font=FONT)


    def level_up(self):
        self.level +=1
        self.clear()
        self.current_level()
    def game_over(self):
        self.goto(-100, 0)
        self.write("Game Over", font=FONT)