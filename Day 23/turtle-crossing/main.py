import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

me = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(me.turtle_move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()

    # detect with car
    for cars in car.all_cars:
        if cars.distance(me) < 20:
            game_is_on = False
            score.game_over()

    # detect me succefully and update score
    if me.is_it_finish_level() == True:
        me.set_new_level()
        car.level_up()
        score.incress_level()

screen.exitonclick()