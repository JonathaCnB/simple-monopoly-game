import random


class Behaviors:
    def __init__(
        self, property_value: float, property_rent: float, balance: float
    ) -> None:
        self.property_value = property_value
        self.property_rent = property_rent
        self.balance = balance

    def impulsive(self) -> bool:
        if self.property_value <= self.balance:
            return True
        return False

    def demanding(self) -> bool:
        if self.property_rent > 50:
            return True
        return False

    def cautious(self) -> bool:
        balance_after_purchase = self.balance - self.property_value
        if balance_after_purchase > 80:
            return True
        return False

    def randomized(self) -> bool:
        likelihood = bool(random.randint(0, 1))
        return likelihood
