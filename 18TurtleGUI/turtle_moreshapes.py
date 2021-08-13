# Wed August 11, 2021
# Week 18 - Turtle Graphics
#           Draw a triangle, square, pentagon, hexagon, heptagon,
#           octagon, nonagon,decagon with a random color for each

# Import turtle and modules
from turtle import *
from random import randint

# Create a turtle object
turtle = Turtle()

# Change the shape to an arrow
turtle.shape('arrow')

# Set the colormode to 255
colormode(255)

# Method to make the shapes
def makeShape(turtle):

    # For Loop from 4 to 10 (so for 4-11 to include 10)
    for s in range(3, 11):
        # Get number of sides
        sides = int(s)

        # Calculate distance to move forward
        distance = 75

        # Calculate the angle in degrees
        angle = 360/s

        # Randomize color
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        # Set the pen color
        turtle.pencolor(r,g,b)

        # While Loop for shapes
        while (sides):
            # Turn
            turtle.right(angle)

            # Move forward
            turtle.forward(distance)

            # Decrement sides
            sides -= 1

# Call the method
makeShape(turtle)

# Create a Screen object that exits on close
screen = Screen()
screen.exitonclick()