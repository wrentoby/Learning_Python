import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shape("turtle")
        self.setheading(90)
        self.move_distance = 10
        self.reset_player()


    def movement(self):
        self.new_y = self.ycor() + self.move_distance
        self.new_x = self.xcor()
        self.goto(x=self.new_x,y=self.new_y)

    def reset_player(self):
        self.teleport(0, -280)

    def player_at_finish_line(self):
        if self.ycor() >= 280:
            self.reset_player()
            return True
        else:
            return False
