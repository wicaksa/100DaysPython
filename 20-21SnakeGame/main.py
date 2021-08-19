# Friday August 13, 2021
# Day 20 Program: Building a Snake Game using Python's Turtle GUI.

# Import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import turtle as t
import time

# Constant
X_COR_START = -290
Y_COR_START = 290
MOVE = Y_COR_START * 2
deg = 270

# Create a game variable
gameOn = True

# 1. Create a Screen for the game to play in
gameScreen = t.Screen()
gameScreen.screensize(canvheight=600, canvwidth=600, bg="black")
# Window title = "Snake Game"
gameScreen.title("Snake Game")
# Use tracer() to turn off automatic screen updates
gameScreen.tracer(n=0)

# Draw border
border = t.Turtle()
border.color("white")
border.penup()
border.goto(X_COR_START, Y_COR_START)
border.pendown()

while deg >= 0:
    border.fd(MOVE)
    border.setheading(deg)
    deg -= 90
border.hideturtle()

# 2. Create the snake object
#    Create food
#    Create score board
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3. Create the ability for the user to move snake with button
gameScreen.listen()
gameScreen.onkey(snake.up,"Up")
gameScreen.onkey(snake.down,"Down")
gameScreen.onkey(snake.left,"Left")
gameScreen.onkey(snake.right,"Right")

while(gameOn):
    # update the screen after each snake box moves
    gameScreen.update()
    # Sleep snake for 0.1 s
    time.sleep(0.1)
    # Move Snake
    snake.move()

    # Detect collision: If head of snake (x,y) == food (x,y)
    if snake.head.distance(food) < 15:
        # Move food to a new random location
        food.refresh()
        # Extend snake
        snake.extend()
        # Increase score by 1
        scoreboard.updateScore()

    # Detect collision with wall
    if snake.head.xcor() > 290 or \
            snake.head.xcor() < -290 or \
            snake.head.ycor() > 290 or \
            snake.head.ycor() < -290:
        gameOn = False
        scoreboard.gameOver()

    # Detect collision with tail: Check if the head touches any of the segments in snakeList
    for i in snake.snakeList[1:]:
        if snake.head.distance(snake.snakeList[i]) < 10:
            gameOn = False
            scoreboard.gameOver()

# Screen exit on click
gameScreen.exitonclick()

