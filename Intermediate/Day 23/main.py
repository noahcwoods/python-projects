import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []

# Spawn Player
player = Player()

# Spawn Scoreboard
scoreboard = Scoreboard()

# Input listeners
screen.listen()
screen.onkeypress(player.up, "w")

game_is_on = True
while game_is_on:
    time.sleep(player.difficulty)
    screen.update()

    # Control car spawn
    spawn_controller = random.randint(1, 9)
    if spawn_controller == 2:
        cars.append(CarManager())

    # Control car list
    for car in cars:
        car.move()
        if car.xcor() < -280:
            car.hideturtle()
            cars.remove(car)

        if player.distance(car) <= 23:
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.increase_level()
        player.increase_difficulty()
