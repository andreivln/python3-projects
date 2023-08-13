from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("turtle")
        self.penup()
        self.starting_position()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

