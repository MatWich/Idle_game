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

        self.lemonShop_inc = None
