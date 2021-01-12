# # Code to extract colors from an image
# import colorgram
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

import random
import turtle as t
from turtle import Turtle, Screen

rgb_colors = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
              (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
              (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
              (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187),
              (151, 206, 220)]

tim = Turtle()
screen = Screen()

t.colormode(255)
tim.shape("classic")
tim.speed(10)
initial_position = [-250, -250]

def change_dir(n):
    tim.penup()
    tim.goto(initial_position[0], initial_position[1]+50*n)
    tim.pendown()


def draw_hirst_painting(dimension, size_of_dots, gap_between_dots):
    tim.hideturtle()
    for n in range(dimension):
        change_dir(n)
        for i in range(dimension):
            tim.pencolor(random.choice(rgb_colors))
            if i != dimension - 1:
                tim.dot(size_of_dots)
                tim.penup()
                tim.forward(gap_between_dots)
                tim.pendown()
            else:
                tim.dot(size_of_dots)


dim = int(input("Enter the dimension(Eg:-for 3x3 enter 3): "))
size = int(input("Enter the size of each dot: "))
gap = int(input("Enter the gap between the dots: "))


draw_hirst_painting(dim, size, gap)

screen.exitonclick()
