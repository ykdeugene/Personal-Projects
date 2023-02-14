import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key='Up')

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()
    time.sleep(car_manager.car_speed)
    screen.update()
    # Detect car collision with turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Detect tutle cross
    if player.ycor() > 280:
        player.reset_player()
        car_manager.increase_speed()
        scoreboard.increase_score()

screen.exitonclick()
