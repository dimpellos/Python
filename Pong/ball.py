from turtle import Turtle
from constants import BALL_SHAPE, BALL_COLOUR, BALL_INIT_POSITION, BALL_MOVE_Y, BALL_MOVE_X, BALL_SPEED


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOUR)
        self.penup()
        self.goto(BALL_INIT_POSITION[0], BALL_INIT_POSITION[1])
        self.bounce_direction = 1
        self.paddle_direction = 1
        self.speed(BALL_SPEED)

    def move(self):
        new_x = self.xcor() + BALL_MOVE_X * self.paddle_direction
        new_y = self.ycor() + BALL_MOVE_Y * self.bounce_direction
        self.goto(new_x, new_y)

    def bounce(self):
        self.bounce_direction *= -1

    def paddle_collision(self):
        self.paddle_direction *= -1

    def reset_position(self):
        self.goto(BALL_INIT_POSITION[0], BALL_INIT_POSITION[1])
        self.paddle_collision()

