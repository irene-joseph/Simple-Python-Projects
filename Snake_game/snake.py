from turtle import Turtle, Screen
DEFAULT_SIZE_OF_SNAKE = 3


class Snake:
    def __init__(self):
        self.blocks_list = []
        self.create_snake()
        self.screen = Screen()

    def create_snake(self):
        for i in range(DEFAULT_SIZE_OF_SNAKE):
            block = Turtle(shape="square")
            block.penup()
            block.color("white")
            block.goto(-20 * i, 0)
            self.blocks_list.append(block)

    def move_up(self):
        if self.blocks_list[0].heading() != 270:
            self.blocks_list[0].setheading(90)

    def move_down(self):
        if self.blocks_list[0].heading() != 90:
            self.blocks_list[0].setheading(270)

    def move_right(self):
        if self.blocks_list[0].heading() != 180:
            self.blocks_list[0].setheading(0)

    def move_left(self):
        if self.blocks_list[0].heading() != 0:
            self.blocks_list[0].setheading(180)

    def move(self):
        for i in range(len(self.blocks_list) - 1, 0, -1):
            self.blocks_list[i].goto(self.blocks_list[i - 1].position())
        self.blocks_list[0].forward(20)
        self.screen.listen()
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.move_left, "Left")

    def reset(self):
        for each in self.blocks_list:
            each.goto(1000,1000)
        self.blocks_list.clear()
        self.create_snake()

    def increase_size(self):
        new_block = Turtle(shape="square")
        new_block.penup()
        new_block.color("white")
        new_block.goto(x=self.blocks_list[0].xcor() + (-20 * len(self.blocks_list)),
                       y=self.blocks_list[0].xcor() + (-20 * len(self.blocks_list)))
        self.blocks_list.append(new_block)
