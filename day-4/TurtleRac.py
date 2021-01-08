# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.pensize(2)
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.forward(-10)
#
#
# def rotate_anticlockwise():
#     tim.left(10)
#
#
# def rotate_clockwise():
#     tim.left(-10)
#
#
# def clear_screen():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()
#
#
#
#
# screen = Screen()
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkeyrelease(key="a", fun=rotate_anticlockwise)
# screen.onkeyrelease(key="d", fun=rotate_clockwise)
# screen.onkey(key="c", fun=clear_screen)
# screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgpic("grass.gif")

is_race_on = False
color_list = ["orange", "red", "blue", "gold", "violet", "pink", "cyan"]
y_positions = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []
winner = ""


for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Who is going to win the Race? Choose a color - ")

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        new_distance = random.randint(0, 10)
        turtle.forward(new_distance)
        if turtle.xcor() > 230:
            winner = turtle.color()
            is_race_on = False

if winner[0] == user_bet:
    print(f"You win the Bet, {user_bet} wins!")
else:
    print(f"You lose the bet, {winner[0]} wins!")


screen.exitonclick()
