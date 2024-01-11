from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 24, "normal"

with open('highscore.txt') as file:
    highscore = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = highscore
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
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}",
                   False,
                   align=ALIGNMENT,
                   font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.update_board()
