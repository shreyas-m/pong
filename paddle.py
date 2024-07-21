from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = None
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shapesize(4, .5)
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
