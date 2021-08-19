from turtle import Turtle
import random

# Constants
SIZE = 1.0

# inherit from the Turtle class
class Food(Turtle):
    
    """
    This class represents the food object on the screen.
    """
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=SIZE, stretch_wid=SIZE)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # Places food in a random location on the screen
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)




