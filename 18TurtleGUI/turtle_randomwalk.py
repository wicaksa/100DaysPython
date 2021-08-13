# Wed August 11, 2021
# Week 18 - Turtle Graphics
#           Random walk, with a random color

# Import modules
from turtle import Turtle, Screen, colormode
import random

# Create a turtle object
turtle = Turtle()

# Change the turtle to an arrow
turtle.shape('arrow')

# Change to a bigger brush size
turtle.pensize(10)

# Change turtle speed
turtle.speed(10)

# Set the colormode
colormode(255)

# Generates a Random Color
def randomColor():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r,g,b)

# Generates a Random direction
def randomDirection():
    # Create a list of random direction
    direction = [0, 90, 180, 270]
    return (random.choice(direction))

# Generates a Random walk
def randomWalk(turtle):
    # Create a distance variable
    distance = 50

    for i in range(0, 50):
        # Generate random color
        random_color = randomColor()
        turtle.pencolor((random_color))

        # Get a random direction
        dir = randomDirection()

        # Turn to that direction
        turtle.right(dir)

        # Move foward
        turtle.fd(distance)

# Call method
randomWalk(turtle)

# Create the Screen object
screen = Screen()
screen.exitonclick()