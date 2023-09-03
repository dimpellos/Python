from turtle import Turtle
from constants import SCOREBOARD_COLOUR, SCOREBOARD_ALIGN, SCOREBOARD_FONT, SCOREBOARD_POSITION


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCOREBOARD_COLOUR)
        self.penup()
        self.goto(SCOREBOARD_POSITION[0], SCOREBOARD_POSITION[1])
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
