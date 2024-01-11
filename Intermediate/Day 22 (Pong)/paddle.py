from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shapesize(1, 5, 1)
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.speed("fastest")
        self.goto(pos)
        self.color("white")


    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)
