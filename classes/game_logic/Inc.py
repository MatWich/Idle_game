import threading


class Inc:
    def __init__(self, name, time, profit, inc_per_upgrade, upgrade_cost, index ,image):
        self.name = name
        self.time = time
        self.profit = profit
        self.inc_per_upgrade = inc_per_upgrade
        self.upgrade_cost = upgrade_cost
        self.image = image
        self.upgrades_no = 0
        self.index = index
        #self.thread.start()
        """ GUI"""
        self.pr_bar = None
        self.image_lbl = None
        self.upgrade_btn = None
        self.upgrades_no_lbl = None
        self.layout = None
        self.active = False

    def upgrade(self):
        self.profit += self.inc_per_upgrade
