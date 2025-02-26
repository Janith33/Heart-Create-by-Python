import math
from turtle import *

# Heart curve functions
def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

# Turtle setup
speed("fastest")
bgcolor("black")
color("red")
penup()  # Lift the pen to prevent drawing while moving to the start point

# Start drawing the heart
for i in range(360):  # 360 steps to make a smooth curve
    t = math.radians(i)  # Convert angle to radians
    x = heart_x(t) * 10  # Scale the X coordinate
    y = heart_y(t) * 10  # Scale the Y coordinate
    goto(x, y)
    pendown()  # Put the pen down to start drawing

# Hide the turtle and finish
hideturtle()
done()
