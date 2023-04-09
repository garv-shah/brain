from turtle import *

screen = Screen()

speed(0)
screen.delay(0)
tracer(0, 0)
bgcolor("black")
pensize(2)
colour_list = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]

# Repeat the following code 5 times (to loop through all the colours in the list above)

def draw_circle(size):
    for i in range(15):
        update()
        for j in colour_list:
            color(j)
            left(5)  # Slightly change the angle of each new square that is drawn
            # Draw a single square
            for k in range(4):
                forward(size)
                left(90)
    draw_circle(size * (2/3))


hideturtle()
draw_circle(300)

screen.exitonclick()
