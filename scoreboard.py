from turtle import Turtle


def game_over(param):
    flash = Turtle()
    flash.color("white")
    flash.hideturtle()
    flash.goto(0, 0)
    flash.write(f"Game Over. {param} won.", False, "center", ("Comic Sans MS", 50, "bold"))


class Scoreboard(Turtle):
    l_score = 0
    r_score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 280)
        self.write(self.l_score, False, "center", ("Comic Sans MS", 70, "normal"))
        self.goto(100, 280)
        self.write(self.r_score, False, "center", ("Comic Sans MS", 70, "normal"))

    def l_scored(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_scored(self):
        self.r_score += 1
        self.update_scoreboard()


