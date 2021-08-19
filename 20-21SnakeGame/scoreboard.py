from turtle import Turtle

# Constants
X_COR = 0
Y_COR = 300
FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"

class Scoreboard(Turtle):
    
    """
    This class keeps track of the score of the game.
    """
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(X_COR, Y_COR)
        self.pendown()
        self.color("white")
        self.score = 0
        self.writeScore()
        self.hideturtle()

    # Updates the score in the game.
    def updateScore(self):
        self.score += 1
        self.clear()
        self.writeScore()

    # Writes the Score on the screen.
    def writeScore(self):
        self.write(arg=f"Score : {self.score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    # Writes the Game over Screen.
    def gameOver(self):
        self.goto(0, 0)
        self.pendown()
        self.color("white")
        self.write(arg="Game Over",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)
