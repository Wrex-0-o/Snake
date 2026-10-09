from turtle import Turtle
SCORE = 0
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):   

    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.scoreUpdate()

    def scoreUpdate(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.clear()
        self.score += 1
        self.scoreUpdate()
