from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_cars()

    def spawn_cars(self):
        for i in range(0, 30):
            self.car = Turtle("square")
            self.car.penup()
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.color(choice(COLORS))
            self.car.setposition(randint(-100, 500), randint(-220, 270))
            self.move_cars()
            self.cars_list.append(self.car)

    def move_cars(self):
        for cars in self.cars_list:
            cars.setheading(180)
            cars.forward(self.car_speed)
            if cars.xcor() < -300:
                cars.goto(randint(300, 500), randint(-220, 270))

    def increment_speed(self):
        self.car_speed += MOVE_INCREMENT