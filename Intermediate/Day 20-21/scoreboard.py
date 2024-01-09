from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 24, "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("White")
        self.penup()
        self.setpos(0, 250)
        self.update_board()
        self.hideturtle()

    def add_point(self):
        self.score += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   False,
                   align=ALIGNMENT,
                   font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
