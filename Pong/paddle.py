from constants import *
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, init_position):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.shapesize(stretch_wid=PADDLE_WID, stretch_len=PADDLE_LEN)
        self.color(PADDLE_COLOUR)
        self.penup()
        self.goto(init_position[0], init_position[1])

    def up(self):
        new_y = self.ycor() + PADDLE_MOVE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_MOVE
        self.goto(self.xcor(), new_y)
