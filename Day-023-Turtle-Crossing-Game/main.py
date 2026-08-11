import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

car_manager = CarManager()
level = Scoreboard()

player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()
            break
            
    
    if player.is_at_finish_line():
        player.reset_position()
        level.increase_level()    
        car_manager.level_up()
    
    
screen.exitonclick()
