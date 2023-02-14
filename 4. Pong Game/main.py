from turtle import Screen
import time
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
R_START_POS = (350, 0)
L_START_POS = (-350, 0)
# import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game 3000")
screen.tracer(0)

scoreboard = Scoreboard()

l_paddle = Paddle(L_START_POS)
r_paddle = Paddle(R_START_POS)
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
    # detect if paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score(0)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score(1)

screen.exitonclick()
