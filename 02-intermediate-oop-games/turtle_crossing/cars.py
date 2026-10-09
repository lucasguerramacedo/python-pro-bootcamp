from turtle import Turtle
import random
COLORS = ("red", "green", "blue", "yellow", "cyan", "magenta", "pink")
START_SPEED = 5
ACCELERATION = 2

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_SPEED
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len= 2, stretch_wid= 1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            for _ in range(5):
                y_pos = random.randrange(-250, 250)
                x_pos = random.randrange(300, 320)
                new_car.goto(x_pos, y_pos)
                cars_near_spawn = [car for car in self.all_cars if car.xcor() > 250]
                if all(new_car.distance(car) > 30 for car in cars_near_spawn):
                    self.all_cars.append(new_car)
                    return
                new_car.hideturtle()
    def car_move(self):
        for car in self.all_cars[:]:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)
    def accelerate(self):
        self.car_speed += ACCELERATION

    def reset_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()

