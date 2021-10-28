from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.value} Highscore = {self.highscore}", move=False, align=ALIGNMENT, font= FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))
        self.write(arg=f"Score = {self.value} Highscore = {self.highscore}", move=False, align=ALIGNMENT, font= FONT)

    def score_change(self):
        self.value += 1
        self.update_scoreboard()

    def reset(self):
        if self.highscore < self.value:
            self.highscore = self.value
        self.value = 0
        self.update_scoreboard()

    # def game_over(self):
    #     game_over = Turtle()
    #     game_over.color("white")
    #     game_over.write(arg=f"Game Over\nYour Score: {self.value}", align=ALIGNMENT, font=FONT)
