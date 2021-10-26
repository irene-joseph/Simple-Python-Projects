from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_SPEED = 0.1


class CarManager():
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.speed = 0.1

    def car_generator(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_dist_x = 300  # random.randint(125, 300)
            random_dist_y = random.randint(-230, 250)
            car.goto(random_dist_x, random_dist_y)
            self.car_list.append(car)

    def move_cars(self):
        for each in self.car_list:
            each.backward(MOVE_INCREMENT)

    def speed_up(self):
        self.speed *= 0.9
