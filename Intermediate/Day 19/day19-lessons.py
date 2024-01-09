import random
from turtle import Turtle, Screen

colors = ["red",
          "orange",
          "yellow",
          "green",
          "blue",
          "purple",
          ]


def main():
    screen = Screen()
    screen.setup(width=500, height=400)

    turtles = []
    for i in range(6):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(-225, (-125 + (i * 50)))

    choice = screen.textinput(title="Make your bet!",
                     prompt="Which turtle will win the race?")

    if choice:
        done = False

    while not done:
        for turtle in turtles:
            if turtle.xcor() > 230:
                done = True
                if choice == turtle.pencolor():
                    print("You Win!")
                else:
                    print("You Lose!")
                print(f"The winning turtle was {turtle.pencolor()}")

            distance = random.randint(0, 10)
            turtle.forward(distance)

    screen.exitonclick()

if __name__ == "__main__":
    main()
