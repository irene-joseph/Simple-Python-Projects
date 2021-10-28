from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

game_is_on = True
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Check the distance from first block to food
    if snake.blocks_list[0].distance(food) < 16:
        food.position_change()
        snake.increase_size()
        score.score_change()
    # Detect Collision with Wall
    head = snake.blocks_list[0]
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        #game_is_on = False
        score.reset()
        snake.reset()
    # Detect Collision with tail
    for each in snake.blocks_list[1:]:
        if head.distance(each) < 10:
            #game_is_on = False
            score.reset()
            snake.reset()


screen.exitonclick()
