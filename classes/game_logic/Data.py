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

        self.lemonShop_inc = Inc("Lemon Shop", 5, 1, 1, 1, LEMON_IMG)
        self.paper_inc = Inc("News Paper Shop", 10, 2, 2, 2, PAPER_IMG)
        self.car_wash_inc = Inc("Car Wash", 15, 3, 3, 2, CAR_IMG)
        self.pizza_inc = Inc("Pizza", 20, 4, 4, 4, PIZZA_IMG)
        self.donut_inc = Inc("Donut Shop", 25, 5, 5, 5, DONUT_IMG)
        self.sea_food_inc = Inc("Sea Food Rest", 30, 6, 6, 6, SHRIMP_IMG)
        self.hokey_inc = Inc("Hokey Club", 35, 7, 7, 7, HOKEY_IMG)
        self.camera_inc = Inc("Cinema", 40, 8, 8, 8, CINEMA_IMGS)
        self.white_house_inc = Inc("White House", 45, 9, 9, 9, HOUSE_IMG)
        self.oil_inc = Inc("Oil Company", 50, 10, 10, 10, OIL_IMG)
