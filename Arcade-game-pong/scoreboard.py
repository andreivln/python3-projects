from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.goto(x=0, y=260)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.left_score} | {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.left_score += 1
        self.update_score_board()

    def increase_score_right(self):
        self.right_score += 1
        self.update_score_board()

