import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    dead = False
    while not dead:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_point()
            snake.add_segment()

        # Detect wall collision
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            dead = True
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            # if segment == snake.head:
            #     pass
            # elif snake.head.distance(segment) < 10:
            #     dead = True
            #     scoreboard.game_over()
            if snake.head.distance(segment) < 10:
                dead = True
                scoreboard.game_over()




    screen.exitonclick()


if __name__ == "__main__":
    main()