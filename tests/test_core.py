import unittest

from core.behaviors import Behaviors


class TestBehaviors(unittest.TestCase):
    def setUp(self) -> None:
        property_value = 80.00
        property_rent = 32.00
        balance = 300.00
        self.behaviors = Behaviors(property_value, property_rent, balance)
        return super().setUp()

    def test_impulsive_behavior_buying(self):
        """
        impulsive behavior buying when the value of the property
        is less than or equal to the balance
        """
        impulsive = self.behaviors.impulsive()
        self.assertTrue(impulsive)

    def test_demanding_behavior_buying(self):
        """
        demanding behavior only buys if the rent is more than 50
        """
        demanding = self.behaviors.demanding()
        self.assertFalse(demanding)

    def test_cautious_behavior_buying(self):
        """
        cautious behavior buys any property as long as there
        is a balance of 80
        """
        cautious = self.behaviors.cautious()
        self.assertTrue(cautious)

    def test_randomized_behavior_buying(self):
        """
        random behavior has a 50% chance of buying the property
        """
        randomized = Behaviors.randomized()
        expected = [True, False]
        self.assertIn(randomized, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
