from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("data.txt", mode="r") as file:
    file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read()) 
        self.goto(x=0, y=260)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}") 

        self.score = 0
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()


