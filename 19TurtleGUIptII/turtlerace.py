# Friday August 13, 2021
# Day 19 Program: Creating a turtle race with turtle gui.

# Import the turtle module
from turtle import *
import random

# Create a Screen
screen = Screen()

# change the screensize
screen.screensize(canvwidth=1000, canvheight=1000, bg="white")

# Create window title
screen.title("Turtle Race")

# Create a list of possible colors
colors = ["green", "red", "yellow", "orange", "blue", "black"]
# Create a list of possible Y-coordinates
ycoorList = [90, 60, 30, 0, -30, -60]
# Create a list of tutles to keep track of them
turtleList  = []

# Create 6 turtles with different colors
for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.setposition(x=-400,y=ycoorList[i])
    turtleList.append(turtle)

# Function to move turtle a random distance
def moveRandom():
    distance = [0, 5, 10, 15, 20, 25, 30]
    randomDistance = random.choice(distance)
    return randomDistance

# Move turtle forward at a random distance
while (turtle.xcor() < 250):
    for turtle in turtleList:
        turtle.forward(moveRandom())

# Screen exit on click
screen.exitonclick()