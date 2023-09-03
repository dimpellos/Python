from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import COLLISION_DISTANCE
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game 3310")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Snake Collision with food
    if snake.head.distance(food) < COLLISION_DISTANCE:
        # TODO: delete food
        # create new food
        food.refresh()
        # score
        scoreboard.increase_score()
        # TODO: make snake bigger



screen.exitonclick()
