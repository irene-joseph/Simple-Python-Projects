from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(10)
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

    def position_change(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))