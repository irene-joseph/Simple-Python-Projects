from turtle import  Turtle
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score = {self.score}", align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 40, "normal"))

    def refresh(self):
        self.score = 0
        self.update()
