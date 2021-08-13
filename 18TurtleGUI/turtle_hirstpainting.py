# Date: Wed August 11, 2021
# Week: Week 18 - Turtle Graphics
# Program: Creating a Hirst painting using Python Turtle and cologram library

# Import libraries
from turtle import Turtle, Screen, colormode
import colorgram
import random

# Extract 10 colors from an image into a tuple
image_colors = colorgram.extract('hirstpainting.jpg', 30)

# Will contain a list of tuples with colors in them
colors = []

# Extract rgb colors
for color in image_colors:
    # Extract each r,g,b tuple
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.g
    tup = (r, g, b)
    # add tuple to rgb_colors
    colors.append(tup)

# Debug print colors
# print(colors)

# change colormode to 255
colormode(255)

# Create a screen
screen = Screen()
screen.screensize(canvwidth=400, canvheight=400,bg="white")

# Create a turtle object
turtle = Turtle()

# Change the speed of the turtle
v = 100
turtle.speed(v)

# Set coordinates
x = -400
y = 360

# Move turtle to top left of screen
turtle.penup()
turtle.goto(x,y)
turtle.pendown()

# Create variable for Y coordinate


# For loop to draw dots across the page
for row in range (0, 10, 1):
    # For loop to go across
    for col in range(0, 10, 1):
        # Get Random color
        color = random.choice(colors)
        # Change pencolor
        turtle.pencolor(color)
        # Make dot with the turtle
        turtle.dot(25)
        # Lift up pen
        turtle.penup()
        # Move 100 Spaces
        turtle.forward(50)
        # Put pen down
        turtle.pendown()
    # Pen up
    turtle.penup()
    # Go to second column
    y -= 60
    # Move pen to next line
    turtle.goto(x, y)
    # Pen down
    turtle.pendown()

# Create a screen that exists on click
screen.exitonclick()

