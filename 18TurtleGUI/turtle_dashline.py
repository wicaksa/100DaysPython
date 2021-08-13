# Wed August 11, 2021
# Week 18 - Turtle Graphics
#           Making a dashed line
#           You can use .penup() or pendown()

# Import turtle module
from turtle import Turtle, Screen

# Create turtle object
turtle = Turtle()

# Change the shape of the turtle object
turtle.shape('arrow')

# method that creates a dashed line
# input: turtle object
# output: turtle creating a dashed black and white line

def turtleDash(turtle):
    # Create a variable for the distance
    dist = 10

    # Create a loop to make a dash
    dashes = 20
    while (dashes):
        # Change color to black
        turtle.pencolor('black')

        # Go forward for x amount in BLACK
        turtle.fd(dist)

        # Change color to white
        turtle.pencolor('white')

        # Go forward for x amount in WHITE
        turtle.fd(dist)

        # Decrement dashes
        dashes -= 1

# Call the method
turtleDash(turtle)

# Create a screen object that exits on click
screen = Screen()
screen.exitonclick()