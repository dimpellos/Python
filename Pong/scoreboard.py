from turtle import Turtle
from constants import SCOREBOARD_COLOUR, SCOREBOARD_ALIGN, SCOREBOARD_FONT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOUR)
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)

    def left_point(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)
