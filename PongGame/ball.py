import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(x=0,y=0)
        self.x_move=10
        self.y_move=10



    def ball_movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x,y=new_y)



    def bounce_y(self):
        self.y_move = self.y_move *(-1)

    def bounce_x(self):
        self.x_move = self.x_move *(-1)

    def reset(self):
        self.teleport(0,0)
        self.bounce_x()

    def increase_ballspeed(self):
        if self.x_move > 0:
            self.x_move += 2.5
        else:
            self.x_move -= 2.5

        if self.y_move > 0:
            self.y_move += 2.5
        else:
            self.y_move -= 2.5