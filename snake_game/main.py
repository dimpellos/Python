from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import COLLISION_FOOD, COLLISION_BORDER, COLLISION_TAIL
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
    if snake.head.distance(food) < COLLISION_FOOD:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Snake collision with borders
    if snake.head.xcor() > COLLISION_BORDER or snake.head.xcor() < -COLLISION_BORDER or snake.head.ycor() > COLLISION_BORDER or snake.head.ycor() < -COLLISION_BORDER:
        gameIsOn = False
        scoreboard.game_over()

    # Snake collision with its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < COLLISION_TAIL:
            gameIsOn = False
            scoreboard.game_over()

screen.exitonclick()
