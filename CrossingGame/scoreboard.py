import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.update_level()

    def update_level(self):
        self.hideturtle()
        self.clear()
        self.color("white")
        self.penup()
        self.current_level += 1
        self.goto(x=-230, y=260)
        self.write(
            arg=f"Level : {self.current_level}",
            align="center",
            font=("cascadia code", 12, "bold")
        )

    def intermission_card(self):
        self.clear()
        self.goto(x=0,y=0)
        self.write(arg=f"Level {self.current_level} Cleared",
                   align="center",
                   font=("cascadia code",12,"normal"))

    def game_over_text(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"""Game Over!!!\nYou completed {self.current_level} Levels"""
                   ,align="center",
                   font=("cascadia code", 12, "normal"))