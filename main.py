from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_is_on = True
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("SNAKE GAME")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_blocks()
        score.update_count()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.update_high_score()
        snake.snake_position()

    for block in snake.block_list[1:]:
        if snake.head.distance(block) < 10:
            score.update_high_score()
            snake.snake_position()

my_screen.exitonclick()