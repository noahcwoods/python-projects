from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def main():
    # Create the screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    # Create the paddle
    paddle_2 = Paddle((350, 0))
    paddle_1 = Paddle((-350, 0))

    # Create the ball
    ball = Ball()

    # Create the scoreboard
    scoreboard = Scoreboard()

    speed = 0.1
    done = False
    while not done:
        # Update the changes on screen
        screen.update()

        # Move ball
        ball.move()

        time.sleep(speed)

        # listeners
        screen.listen()
        screen.onkeypress(paddle_1.up, "w")
        screen.onkeypress(paddle_1.down, "s")

        screen.onkeypress(paddle_2.up, "Up")
        screen.onkeypress(paddle_2.down, "Down")

        # Detect collision with paddle
        if ball.distance(paddle_2) < 50 and ball.xcor() > 320 or ball.distance(paddle_1) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            if speed - .005 <= 0:
                pass
            elif speed - .005 > 0:
                speed = speed - .005


        # Detect collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect point score
        if ball.xcor() > 380:
            scoreboard.increase_l_score()
            ball.reset_position()
            speed = 0.1
        if ball.xcor() < -380:
            scoreboard.increase_r_score()
            ball.reset_position()
            speed = 0.1

    # Exit screen
    screen.exitonclick()


if __name__ == '__main__':
    main()
