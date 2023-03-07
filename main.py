import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()


screen.listen()
screen.colormode(255)
screen.onkey(player.move, "Up")

wave = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    wave.move_cars()
    if player.ycor() > 300:
        scoreboard.increase_score()
        wave.increment_speed()
        player.reset_player()

    for car in wave.cars_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()