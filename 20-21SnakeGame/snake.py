from turtle import *

# CONSTANT VARIABLES
STARTING_X = [0, -20, -40] # a list of x coordinates for the starting snake positions
MOVE_DIST = 20 # moves turtle a certain amount of spaces
# Degrees to set turtle heading
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A snake class that represents the main object in the snake game."""

    # Initialize starting position
    def __init__(self):
        # an empty list that will append newly created snake objects
        self.snakeList = []
        self.createSnake() # Constructor
        self.head = self.snakeList[0]

    def createSnake(self):
        for i in range(0, 3):
            # create a new snake object
            snake = Turtle(shape="square")
            # move pen up so you don't get any lines
            snake.penup()
            # set the x position using coordinates for the list
            snake.setpos(x=STARTING_X[i], y=0)
            # change the snake color
            snake.color("white")
            # add snake to snake list
            self.snakeList.append(snake)

    # Moves the snake automatically by MOVE_DIST paces
    def move(self):
        # C B A
        # Move C -> B, B -> A, and A -> new location
        # Loop from last segment to first segment
        for i in range(len(self.snakeList) - 1, 0, -1):
            # Move last segment to the next segment's position for all of the segments
            new_x = self.snakeList[i - 1].xcor()
            new_y = self.snakeList[i - 1].ycor()
            self.snakeList[i].goto(new_x, new_y)
        # Move the first segment
        self.head.fd(MOVE_DIST)
    # Make sure the snake can't move in the opposite direction
    # Sets the snake direction to North
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Sets the snake direction to South
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Sets the snake direction to West
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

     # Sets the snake direction to East
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Extend snake by 1
    def extend(self):
        snake = Turtle(shape="square")
        snake.penup()
        X_COR = self.snakeList[-1].xcor()
        Y_COR = self.snakeList[-1].ycor()
        snake.goto(X_COR, Y_COR)
        snake.color("white")
        self.snakeList.append(snake)
        
