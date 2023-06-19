import turtle
import math


# draw recursive square
def draw_square(size):
    turtle.forward(size)
    turtle.right(90)
    for i in range(2):
        turtle.forward(size)
        turtle.right(90)
    turtle.forward(size/10 * 9)
    turtle.right(90)

    if size > 1:
        draw_square(size/10 * 9)


draw_square(300)
