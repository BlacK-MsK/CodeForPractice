from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        # self.goto(-100, 200)
        # self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # self.goto(100, 200)
        # self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_score_update(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_score_update(self):
        self.r_score += 1
        self.update_scoreboard()

