import unittest

from core.behaviors import Behaviors


class TestBehaviors(unittest.TestCase):
    def test_impulsive_behavior_buying(self):
        """
        impulsive behavior buying when the value of the property
        is less than or equal to the balance
        """
        property_value = 80.00
        balance = 300.00
        impulsive = Behaviors.impulsive(property_value, balance)
        self.assertTrue(impulsive)

    def test_demanding_behavior_buying(self):
        """
        demanding behavior only buys if the rent is more than 50
        """
        property_rent = 80.00
        demanding = Behaviors.demanding(property_rent)
        self.assertTrue(demanding)

    def test_cautious_behavior_buying(self):
        """
        cautious behavior buys any property as long as there
        is a balance of 80
        """
        property_value = 80.00
        balance = 300.00
        cautious = Behaviors.cautious(property_value, balance)
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
