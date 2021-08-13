# Friday August 13, 2021
# Day 19
# Program: An etch a sketch game using turtle GUI.

"""
Key strokes:
w = forward
s = backwards
a = counter clockwise
d = clockwise
c = clear drawing
"""

# Import the turtle module
from turtle import *

# Create turtle
turtle = Turtle()

# Change turtle speed
turtle.speed("fastest")

# Create screen
screen = Screen()

# Create functions
def moveForwards():
    turtle.fd(10)
def moveBackwards():
    turtle.bk(10)
def moveCounterclockwise():
    # Turn turtle left
    turtle.left(10)
def moveClockwise():
    # Turn turtle right
    turtle.right(10)
def clearScreen():
    # clear screen
    turtle.clear()
    # put turtle back in middle
    turtle.reset()

# Create on screen listener
screen.listen()

# Create onclick functions
screen.onkey(fun=moveForwards, key='w')
screen.onkey(fun=moveBackwards, key='s')
screen.onkey(fun=moveCounterclockwise, key='a')
screen.onkey(fun=clearScreen, key='c')

# Create exit on click
screen.exitonclick()