import time
import turtle
from math import gamma

import cars
import player
import scoreboard

#this is good
the_screen = turtle.Screen()
the_screen.setup(600,600)
the_screen.bgcolor("black")
the_screen.tracer(0)
the_screen.title(titlestring="the crosser game")

the_score = scoreboard.Scoreboard()

#good
tim = player.Player()
the_screen.listen()
the_screen.onkey(fun=tim.movement,key="w")

the_car = cars.Cars()
game_over  = False

while not game_over:
    the_screen.update()
    time.sleep(0.1)

    the_car.create_car()
    the_car.move_cars()


    for i in the_car.all_cars :
        if tim.distance(i) <= 20:
            the_score.game_over_text()
            the_car.clear_cars()
            tim.hideturtle()
            the_screen.update()
            game_over = True


    if tim.player_at_finish_line():
        the_car.clear_cars()
        the_score.intermission_card()
        the_screen.update()
        time.sleep(3)
        the_car.start_next_level()
        the_score.update_level()



the_screen.exitonclick()