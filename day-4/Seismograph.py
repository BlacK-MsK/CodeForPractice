import turtle as t
import random

"""timmy_the_turtle = Turtle()
while True:
    timmy_the_turtle.speed(1)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    if abs(timmy_the_turtle.pos()) < 1:
        break


tim = Turtle()
tim.color("red")
for _ in range(20):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()"""
"""
triangle = Turtle()
triangle.color("purple")
while True:
    triangle.forward(100)
    triangle.left(120)
    if abs(triangle.pos()) < 1:
        break

square = Turtle()
square.color("gold")
while True:
    square.forward(100)
    square.left(90)
    if abs(square.pos()) < 1:
        break

pentagon = Turtle()
pentagon.color("pink")
while True:
    pentagon.forward(100)
    pentagon.left(72)
    if abs(pentagon.pos()) < 1:
        break

hexagon = Turtle()
hexagon.color("green")
while True:
    hexagon.forward(100)
    hexagon.left(60)
    if abs(hexagon.pos()) < 1:
        break

heptagon = Turtle()
heptagon.color("magenta")
while True:
    heptagon.forward(100)
    heptagon.left(51.43)
    if abs(heptagon.pos()) < 1:
        break

octagon = Turtle()
octagon.color("blue")
octagon.pensize(10)
while True:
    octagon.forward(100)
    octagon.left(45)
    if abs(octagon.pos()) < 1:
        break

nonagon = Turtle()
nonagon.color("red")
while True:
    nonagon.forward(100)
    nonagon.left(40)
    if abs(nonagon.pos()) < 1:
        break

decagon = Turtle()
while True:
    decagon.forward(100)
    decagon.left(36)
    if abs(decagon.pos()) < 1:
        break
"""
"""t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


angle = [0, 90, 180, 270]
tim = t.Turtle()
tim.pensize(10)
tim.speed("fastest")
for _ in range(500):
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(angle))

screen = t.Screen()
screen.exitonclick()
"""

t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


tim = t.Turtle()
tim.speed("fastest")
for _ in range(120):
    tim.color(random_colour())
    tim.circle(radius=200)
    tim.setheading(tim.heading()+3)

screen = t.Screen()
screen.exitonclick()
