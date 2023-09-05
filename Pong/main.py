from turtle import Screen
from constants import SCREEN_COLOUR, SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_LEFT_INIT,\
    PADDLE_RIGHT_INIT, SCREEN_TRACER, BALL_BOUNCE, PADDLE_DISTANCE, PADDLE_XCOR_DISTANCE
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOUR)
screen.title(SCREEN_TITLE)
screen.tracer(SCREEN_TRACER)

r_paddle = Paddle(PADDLE_RIGHT_INIT)
l_paddle = Paddle(PADDLE_LEFT_INIT)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game = True
while game:
    time.sleep(0.1)
    screen.update()

    ball.move()

    # Ball collision with ceiling/floor
    if ball.ycor() > BALL_BOUNCE or ball.ycor() < -BALL_BOUNCE:
        ball.bounce()

    # Ball collision with r_paddle
    if (ball.distance(r_paddle) < PADDLE_DISTANCE and ball.xcor() > PADDLE_XCOR_DISTANCE) or (ball.distance(l_paddle) < PADDLE_DISTANCE and ball.xcor() < -PADDLE_XCOR_DISTANCE):
        ball.paddle_collision()

    if ball.xcor() > PADDLE_XCOR_DISTANCE +40:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -PADDLE_XCOR_DISTANCE -40:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
