import unittest

from core.property import Property


class TestProperties(unittest.TestCase):
    def setUp(self) -> None:
        self.property1 = Property(1)
        return super().setUp()

    def test_property_attr_position_has_a_correct_value(self):
        self.assertEqual(self.property1.position, 1)

    def test_property_attr_owner_has_a_correct_value(self):
        self.assertEqual(self.property1.owner, "")

    def test_property_attr_value_has_a_correct_value(self):
        self.assertGreaterEqual(self.property1.value, 30)
        self.assertLessEqual(self.property1.value, 450)

    def test_property_attr_rent_has_a_correct_value(self):
        rent = round(self.property1.value * 0.4)
        self.assertEqual(self.property1.rent, rent)


if __name__ == "__main__":
    unittest.main(verbosity=2)
