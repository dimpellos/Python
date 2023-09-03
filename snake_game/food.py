from turtle import Turtle
from constants import *
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=FOOD_LEN, stretch_wid=FOOD_WIDTH)
        self.color(FOOD_COLOUR)
        self.speed(FOOD_SPEED)
        # init food
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
