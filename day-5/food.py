from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold")
        self.speed("fastest")
        self.next_food()
        # self.goto(X_FOOD, Y_FOOD)

    def next_food(self):
        x_food = random.randint(-285, 285)
        y_food = random.randint(-285, 285)
        self.goto(x_food, y_food)
