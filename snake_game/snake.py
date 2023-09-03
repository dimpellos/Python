from turtle import Screen, Turtle
from constants import *


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # after creating snake, as segments is empty
        self.head = self.segments[0]
        self.direction = DIRECTION_RIGHT

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_seg = Turtle(SNAKE_SHAPE)
            new_seg.color(SNAKE_COLOUR)
            new_seg.penup()
            new_seg.goto(pos)
            self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.direction != DIRECTION_DOWN:
            self.direction = DIRECTION_UP
            self.head.setheading(self.direction)
        else:
            pass

    def down(self):
        if self.direction != DIRECTION_UP:
            self.direction = DIRECTION_DOWN
            self.head.setheading(self.direction)
        else:
            pass

    def left(self):
        if self.direction != DIRECTION_RIGHT:
            self.direction = DIRECTION_LEFT
            self.head.setheading(self.direction)
        else:
            pass

    def right(self):
        if self.direction != DIRECTION_LEFT:
            self.direction = DIRECTION_RIGHT
            self.head.setheading(self.direction)
        else:
            pass
