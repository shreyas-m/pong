from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move_distance = 10
        self.y_move_distance = 10

    def move(self):
        new_x = self.xcor() + self.x_move_distance
        new_y = self.ycor() + self.y_move_distance
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move_distance *= -1

    def bounce_x(self):
        self.x_move_distance *= -1
        self.move_speed *= .9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
