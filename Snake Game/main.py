from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Wiggly - The Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    #Detect food collision
    if snake.head.distance(food) < 15 :
        food.refresh()
        score_board.increase_score()
        snake.increase_length()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        score_board.game_over()
        game_is_on = False

    #Detect collision with tail
    #if head collides with any segment in the tail
    for segments in snake.snake:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_on = False
            score_board.game_over()

















screen.exitonclick()