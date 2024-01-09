from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            self.add_segment()
            self.head = self.segments[0]

    def add_segment(self):
        if not self.segments:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            return self.segments.append(snake)
        else:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(self.segments[-1].xcor() - 20, 0)
            return self.segments.append(snake)


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_coords = self.segments[i - 1].xcor(), self.segments[i - 1].ycor()
            self.segments[i].goto(new_coords)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)