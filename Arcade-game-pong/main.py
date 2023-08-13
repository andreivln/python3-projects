from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def arcade_game():

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((380, 0))
    left_paddle = Paddle((-380, 0)) 
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(fun=right_paddle.up, key="Up")
    screen.onkeypress(fun=right_paddle.down, key="Down")
    screen.onkeypress(fun=left_paddle.up, key="w")
    screen.onkeypress(fun=left_paddle.down, key="s")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detect Collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            # needs to bounce
            ball.bounce_y()

        # Detect Collusion with right paddle
        if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() < -350:
            ball.bounce_x()


        # Detect when right paddle misses
        if ball.xcor() > 385:
            # game_is_on = False
            scoreboard.increase_score_left()
            ball.game_over()
        # Detect when left paddle misses
        if ball.xcor() < -385:
            scoreboard.increase_score_right()
            ball.game_over()


    screen.exitonclick()


arcade_game()
