from turtle import Turtle
WIDTH = 100/20
LENGTH = 20/20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(WIDTH, LENGTH, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        # maybe put a min and max height?

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        # maybe put a min and max height?