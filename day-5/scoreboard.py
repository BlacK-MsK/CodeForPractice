from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 45, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write(arg=f"Score: 0", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.speed("fastest")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)



