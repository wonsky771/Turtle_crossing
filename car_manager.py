from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.add_car()

    def add_car(self):
        car = Turtle()
        y_pos = random.randint(-250, 250)
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(1, 2)
        car.penup()
        car.goto(320, y_pos)
        self.cars.append(car)

    def move(self):
        for car in self.cars[::6]:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT







