from ultils.for_numbers import random_between


class Property:
    def __init__(self, position: int, owner: str = ""):
        self.position = position
        self.owner = owner
        self.value = random_between(30, 150)
        self.rent = round(self.value * 0.4)
