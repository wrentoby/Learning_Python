import turtle
import paddle
import ball
import time
import scoreboard


my_screen = turtle.Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong - By Wren")
my_screen.tracer(0)

l_paddle = paddle.Paddle((-350,0))
r_paddle = paddle.Paddle((350,0))

my_screen.listen()
my_screen.onkey(key="Up",fun=r_paddle.go_up)
my_screen.onkey(key="w",fun=l_paddle.go_up)
my_screen.onkey(key="Down",fun=r_paddle.go_down)
my_screen.onkey(key="s",fun=l_paddle.go_down)

the_ball = ball.Ball()


my_scoreboard = scoreboard.Scoreboard()
game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    the_ball.ball_movement()



    if the_ball.ycor() > 280 or the_ball.ycor() < -280:
        the_ball.bounce_y()

    if the_ball.distance(r_paddle)<50 and the_ball.xcor() > 320 or the_ball.distance(l_paddle)<50 and the_ball.xcor() < -320:
        the_ball.bounce_x()
        the_ball.increase_ballspeed()

    if the_ball.xcor() > 370 :
        the_ball.reset()
        my_scoreboard.l_point()

    if the_ball.xcor() < -370:
        the_ball.reset()
        my_scoreboard.r_point()


my_screen.exitonclick()
