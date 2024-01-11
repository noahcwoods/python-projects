from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 24, "normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.pencolor("White")
        self.penup()
        self.hideturtle()
        self.setpos(0, 250)
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-80, 250)
        self.write(self.l_score,
                   False,
                   align=ALIGNMENT,
                   font=FONT)
        self.goto(80, 250)
        self.write(self.r_score,
                   False,
                   align=ALIGNMENT,
                   font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.update_board()

    def increase_l_score(self):
        self.l_score += 1
        self.update_board()
