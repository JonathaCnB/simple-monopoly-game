import random


class Behaviors:
    @staticmethod
    def impulsive(property_value: float, balance: float) -> bool:
        if property_value <= balance:
            return True
        return False

    @staticmethod
    def demanding(property_rent: float) -> bool:
        if property_rent > 50:
            return True
        return False

    @staticmethod
    def cautious(property_value: float, balance: float) -> bool:
        balance_after_purchase = balance - property_value
        if balance_after_purchase > 80:
            return True
        return False

    @staticmethod
    def randomized() -> bool:
        likelihood = bool(random.randint(0, 1))
        return likelihood
