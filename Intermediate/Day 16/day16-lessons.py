import turtle
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")

my_screen = Screen()
print(my_screen.canvheight)

timmy.fd(100)
my_screen.exitonclick()