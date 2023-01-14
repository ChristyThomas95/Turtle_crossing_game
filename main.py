from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import Cars
import time


# Creating the Screen for the game
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Cross")
screen.tracer(0)

#calling each class
player = Player()
scoreboard = Scoreboard()
car_manager = Cars()

#movements

screen.listen()
screen.onkey(player.go_up, "Up")


#speed of the game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

#collision and level upgrade point

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finishing_point():
        player.go_to_starting()
        car_manager.level_up()
        scoreboard.increase_level()






screen.exitonclick()