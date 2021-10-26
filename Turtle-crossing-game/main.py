import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
score = Scoreboard()
car_manager = CarManager()
game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(tim.move_up, "Up")
    time.sleep(car_manager.speed)
    screen.update()
    car_manager.car_generator()
    car_manager.move_cars()
    # Detect the end point, update the score and increase the speed of cars
    if tim.ycor() > 250:
        tim.refresh()
        score.update()
        car_manager.speed_up()
    # Detect collision with any of the car
    for each in car_manager.car_list:
        if tim.distance(each) < 20:
            score.game_over()
            game_is_on = False
            user_res = screen.textinput(title="Play Again", prompt="Do you want to play again?")
            if user_res.upper() == "YES":
                game_is_on = True
                tim.refresh()
                score.refresh()

screen.exitonclick()


