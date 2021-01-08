# import colorgram
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
import turtle as t
import random

x = -200
y = -200
tim = t.Turtle()
t.colormode(255)
color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44),
              (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77),
              (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89),
              (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97),
              (222, 177, 182), (109, 128, 151)]
tim.penup()
tim.setposition(-200, -200)
tim.pendown()
tim.speed("fastest")
for _ in range(10):
    for _ in range(10):
        tim.dot(30, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    y += 50
    tim.setposition(x, y)

tim.hideturtle()
screen = t.Screen()
screen.exitonclick()
