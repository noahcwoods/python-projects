import time
from turtle import Turtle, Screen
from snake import Snake


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    dead = False
    while not dead:
        screen.update()
        time.sleep(0.05)
        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()