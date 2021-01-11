from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-385, 0))
r_paddle = Paddle((380, 0))

ball = Ball()

scoreboard = Score()

screen.listen()
screen.onkeypress(fun=l_paddle.move_paddle_up)
screen.onkeypress(key="s", fun=l_paddle.move_paddle_down)
screen.onkeypress(key="Up", fun=r_paddle.move_paddle_up)
screen.onkeypress(key="Down", fun=r_paddle.move_paddle_down)

game_is_on = True
ball_speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # detect collision with paddle
    if ball.xcor() > 360 and ball.distance(r_paddle) < 50 or ball.xcor() < -355 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        ball_speed *= 0.9

    elif ball.xcor() > 400:
        ball.restart()
        r_paddle.restart()
        l_paddle.restart()
        scoreboard.l_score_update()
        time.sleep(3)

    elif ball.xcor() < -400:
        ball.restart()
        r_paddle.restart()
        l_paddle.restart()
        scoreboard.r_score_update()
        time.sleep(3)

screen.exitonclick()
