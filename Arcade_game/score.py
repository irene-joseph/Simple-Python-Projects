from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        for i in range (-300, 300, 50):
            self.goto(0, i)
            self.write(arg="|", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 230)
        self.write(arg=f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(-100, 230)
        self.write(arg=f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def add_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
