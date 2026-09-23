from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.title("pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
tenish = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

game_is_on = True

while game_is_on:
    time.sleep(tenish.move_speed)
    screen.update()
    tenish.move()

    #detect collision with wall
    if tenish.ycor() > 280 or tenish.ycor() < -280:
        #reverce
        tenish.bounce_y()

    # detect collision with paddle
    if tenish.distance(r_paddle) < 50 and tenish.xcor() > 320 or tenish.distance(l_paddle) < 50 and tenish.xcor() < -320:
        tenish.bounce_x()

    if tenish.xcor() > 400:
        tenish.reset_position()
        score.r_point()

    if tenish.xcor() < -400:
        tenish.reset_position()
        score.l_point()

screen.exitonclick()