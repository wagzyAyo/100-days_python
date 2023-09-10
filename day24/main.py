from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.display()
    # Detect collosion with food

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < - 280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < - 280:
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for seg in snake.segment[1:]:
        if snake.snake_head.distance(seg) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
