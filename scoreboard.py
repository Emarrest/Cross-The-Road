FONT = ("JetBrains Mono", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-300, 262)
        self.current_level = 1
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(f"Level:{self.current_level}", font=FONT)

    def increase_score(self):
        self.current_level += 1
        self.current_score()

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("JetBrains Mono", 20, "normal"))