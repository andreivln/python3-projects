import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.cars_move()

    # Detect Collision with car
    for car in car_manager.all_cars: 
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

        # Detect a succesful crossing
    if player.finish():
        player.starting_position()
        car_manager.next_level()
        scoreboard.increase_level()
        scoreboard.update_level()



screen.exitonclick()
