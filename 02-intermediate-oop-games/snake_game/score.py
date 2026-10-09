from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 20, "normal"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("green")
        self.score = 0
        with open("data.txt") as data:
            content = data.read().strip()
            self.high_score = int(content) if content else 0
        self.set_score()
    def set_score(self):
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.high_score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.set_score()
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.set_score()
