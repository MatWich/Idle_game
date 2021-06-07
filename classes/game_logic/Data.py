from .Inc import Inc
from settings import *


class Data:
    _instance = None

    @staticmethod
    def get_instance():
        if Data._instance is None:
            Data()
        return Data._instance

    def __init__(self):
        if Data._instance is not None:
            raise Exception("You cannot create second singleton class")
        else:
            Data._instance = self

        self.lemonShop_inc = Inc("Lemon Shop", 0.05, 1, 1, 1, 1,LEMON_IMG)
        self.paper_inc = Inc("News Paper Shop", .1, 2, 2, 2, 2,PAPER_IMG)
        self.car_wash_inc = Inc("Car Wash", .15, 3, 3, 2, 3,CAR_IMG)
        self.pizza_inc = Inc("Pizza", .2, 4, 4, 4, 4, PIZZA_IMG)
        self.donut_inc = Inc("Donut Shop", .25, 5, 5, 5, 5, DONUT_IMG)
        self.sea_food_inc = Inc("Sea Food Rest", .30, 6, 6, 6, 6, SHRIMP_IMG)
        self.hokey_inc = Inc("Hokey Club", .35, 7, 7, 7, 7, HOKEY_IMG)
        self.camera_inc = Inc("Cinema", .40, 8, 8, 8, 8, CINEMA_IMGS)
        self.white_house_inc = Inc("White House", .45, 9, 9, 9, 9, HOUSE_IMG)
        self.oil_inc = Inc("Oil Company", .50, 10, 10, 10, 10, OIL_IMG)

        self.incs = [self.lemonShop_inc, self.paper_inc, self.car_wash_inc,
                     self.pizza_inc, self.donut_inc, self.sea_food_inc, self.hokey_inc,
                     self.camera_inc, self.white_house_inc, self.oil_inc]

        self.profit = 0
