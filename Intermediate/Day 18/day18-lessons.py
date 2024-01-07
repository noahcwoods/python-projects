import random
import random as r
from turtle import Turtle, Screen, colormode

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral")


# done = False
# count = 3
# while not done:
#     angle = 360 / count
#     for i in range(count):
#         timmy_the_turtle.left(angle)
#         timmy_the_turtle.forward(100)
#     count += 1
#
#     if count == 10:
#         done = True

# done = False
# count = 0
# directions = [0, 90, 180, 270]
# while not done:
#     colormode(255)
#     timmy_the_turtle.speed("fastest")
#     direction = random.choice(directions)
#     random_number = r.randint(1, 3)
#     timmy_the_turtle.pencolor(r.randint(0, 255),
#                               r.randint(0, 255),
#                               r.randint(0, 255))
#     timmy_the_turtle.pensize(25)
#     timmy_the_turtle.setheading(direction)
#     timmy_the_turtle.forward(50)
#     count += 1
#     if count == 500:
#         done = True

def random_color():
    return random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(size_of_gap + timmy_the_turtle.heading())


colormode(255)
timmy_the_turtle.speed("fastest")
draw_spirograph(5)






screen = Screen()
screen.exitonclick()