STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)

    def move(self):
        self.setheading(90)
        self.forward(10)

    def reset_player(self):
        self.goto(0, -280)
