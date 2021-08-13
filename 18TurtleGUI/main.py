# Wednesday August 11, 2021
# Day 18 - Turtle Graphics

# Import the Turtle & Screen modules
from turtle import Turtle, Screen

# Create a new Turtle object
turtle = Turtle()

# Change the shape of the turtle
turtle.shape("turtle")

# Change the color of the turtle
turtle.color("red")

# Move turtle forward by 100 spaces
turtle.fd(100)

# Create a Screen object
# Put it at the bottom after you're done with everything else
screen = Screen()

# Create a Screen that can be closed with a click
screen.exitonclick()

