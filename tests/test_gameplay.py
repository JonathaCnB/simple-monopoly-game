import unittest

from ultils import for_numbers


class TestGamePlay(unittest.TestCase):
    def test_roolin_the_dice_returns_between_1_and_6(self):
        dice = for_numbers.play_dice()
        self.assertGreaterEqual(dice, 1)
        self.assertLessEqual(dice, 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
