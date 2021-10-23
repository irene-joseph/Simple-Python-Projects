from turtle import Turtle, Screen

P_STRETCH_LEN = 1
P_STRETCH_WIDTH = 5
PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self, p_xcor, p_ycor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=P_STRETCH_WIDTH, stretch_len=P_STRETCH_LEN)
        self.goto(x=p_xcor, y=p_ycor)
        self.screen = Screen()

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 20)


