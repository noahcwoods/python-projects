from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("Black")
        self.penup()
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-200, 240)
        self.write(f"Level: {self.score}",
                   False,
                   align="center",
                   font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_board()


