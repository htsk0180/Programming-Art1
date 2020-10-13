import turtle
import time


def curveSection(length=200):
    for _ in range(length):
        turtle.right(1)
        turtle.forward(1)


def halfHeart(angle, forward, left):
    if left:
        turtle.left(angle)
        turtle.forward(forward)
        curveSection()
    else:
        turtle.left(120)
        curveSection()
        turtle.forward(forward)


def draw(angles, forward):
    left = True
    for angle in angles:
        halfHeart(angle, forward, left)
        left = False


angles = [140, 110]
FORWARD = 112

turtle.bgcolor("#e6b94c")
turtle.speed(2)
turtle.color("#8c1c25", "#f25050")
turtle.begin_fill()
turtle.pensize(10)

draw(angles,FORWARD)
turtle.end_fill()
turtle.hideturtle()
