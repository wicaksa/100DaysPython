# Wed August 11, 2021
# Week 18 - Turtle Graphics
#           Making a square

# Import modules
from turtle import Turtle, Screen

# Create a turtle
turtle = Turtle()

# Change turtle to an arrow
turtle.shape('arrow')

# function that moves turtle in a square
# input : turtle object
# output: turtle moves in a square

def turtleSquare(turtle):
    # Create a variable for the distance and angle
    dist = 100
    angle = 90

    # While loop to make a square
    moves = 4
    while(moves > 0):

        # Move turtle forward 100 spaces
        turtle.fd(dist)

        # Turn turtle left
        turtle.left(angle)

        # Move turtle forward 100 spaces
        turtle.fd(dist)

        # Decrement moves
        moves -= 1

# Call the method
turtleSquare(turtle)

# Create a Screen that exits on click
screen = Screen()
screen.exitonclick()