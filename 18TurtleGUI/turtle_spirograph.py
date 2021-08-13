# Date: Wed August 11, 2021
# Week: Week 18 - Turtle Graphics
# Program: Drawing a spirograph using trutle graphics in Python.

# Import modules
from turtle import *
import random

# Create a turtle object
t = Turtle()

# Change the turtle shape
t.shape('arrow')

# Change speed of turtle
t.speed(50)

# Change colormode
colormode(255)

# Set a radius
r = 100

# Set degree
d = 5

# Method to create random color
# Returns a tuple of the rgb spectrum
def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color

# method to draw spirograph
def drawSpirograph(turtle, degree, radius):
    for i in range(0, 360, degree):
        # change pen color
        turtle.pencolor(randomColor())
        # draw circle
        turtle.circle(radius)
        # change the angle by 1 degree
        t.left(degree)

# Call Method
drawSpirograph(t, d, r)

# Create a screen object that exists on click
screen = Screen()
screen.exitonclick()

