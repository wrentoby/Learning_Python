import random
import turtle

# START_SPEED = 5
SPEED_INCREMENT = 10
CAR_COLOURS = ["cyan", "aqua", "turquoise", "deepskyblue", "dodgerblue", "springgreen", "lime", "chartreuse",
               "yellow","gold", "orange", "orangered", "hotpink", "deeppink", "magenta", "violet", "plum", "orchid",
               "red"]

class Cars:
    def __init__(self):
        self.all_cars = []
        self.start_speed = 5

    def create_car(self):
        random_chance = [1]
        if random.randint(1,6) in random_chance:
            new_car = turtle.Turtle()
            new_car.color(random.choice(CAR_COLOURS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.goto(x=car.xcor()-self.start_speed,y=car.ycor())


    def start_next_level(self):
        self.start_speed += SPEED_INCREMENT
        self.clear_cars()

    def clear_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()