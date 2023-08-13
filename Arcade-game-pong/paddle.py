from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):  
        super().__init__()

        # self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.7)
        self.penup()
        self.goto(position)  

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
