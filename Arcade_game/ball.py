from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
       self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def change_y_direction(self):
        self.y_move *= -1

    def change_x_direction(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.change_x_direction()
