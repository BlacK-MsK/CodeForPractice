from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            new_square = Turtle(shape="circle")
            new_square.color("green")
            new_square.penup()
            new_square.goto(positions)
            self.segments.append(new_square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def update_body(self):
        new_x_position = self.segments[len(self.segments)-1].xcor()
        new_y_position = self.segments[len(self.segments) - 1].ycor()
        newPart = Turtle(shape="circle")
        newPart.color("green")
        newPart.penup()
        newPart.goto(new_x_position, new_y_position)
        self.segments.append(newPart)





