from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "s")
screen.onkey(paddle_l.go_down, "x")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y_direction()

    # Detect Collision with paddles
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.change_x_direction()

    # Ball miss and game reset
    # Right player
    if ball.xcor() > 380:
        ball.reset_position()
        score.add_l_score()
    # Left player
    if ball.xcor() < -380:
        ball.reset_position()
        score.add_r_score()




screen.exitonclick()
