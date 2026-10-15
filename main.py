from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#121212")
screen.tracer(0)


#draw walls
top_wall = Turtle("square")
top_wall.color("#dedede")
top_wall.penup()
top_wall.goto(0, 300)
top_wall.shapesize(stretch_wid=.01, stretch_len=30)

bottom_wall = Turtle("square")
bottom_wall.color("#dedede")
bottom_wall.penup()
bottom_wall.goto(0, -300)
bottom_wall.shapesize(stretch_wid=.01, stretch_len=30)

left_wall = Turtle("square")
left_wall.color("#dedede")
left_wall.penup()
left_wall.goto(-300, 0)
left_wall.shapesize(stretch_wid=30, stretch_len=.01)

right_wall = Turtle("square")
right_wall.color("#dedede")
right_wall.penup()
right_wall.goto(300, 0)
right_wall.shapesize(stretch_wid=30, stretch_len=.01)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.spawn_food()
        snake.grow()
        score.point()


    #detect collision with walls
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
