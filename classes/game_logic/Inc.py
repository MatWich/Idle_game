class Inc:
    def __init__(self, name, time, profit, inc_per_upgrade, upgrade_cost, image):
        self.name = name
        self.time = time
        self.profit = profit
        self.inc_per_upgrade = inc_per_upgrade
        self.upgrade_cost = upgrade_cost
        self.image = image
        self.pr_bar = None
        self.active = False

    def upgrade(self):
        self.profit += self.inc_per_upgrade

