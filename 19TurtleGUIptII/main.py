# Friday August 13, 2021
# Day 19 - Action Listeners with Turtle

# Import module
from turtle import Turtle, Screen

# Create a turtle object
turtle = Turtle()

# Create a screen object
screen = Screen()

# Function to move turtle forward
def moveForward():
    turtle.fd(10)

# Create a listener on the screen
screen.listen()

# Call screen onkey function without the ()
screen.onkey(fun=moveForward, key="space")

# Exit on click so that you can close the screen
screen.exitonclick()
