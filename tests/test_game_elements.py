import unittest

from core.board import Board
from core.players import Players
from ultils import for_numbers


class TestGameElements(unittest.TestCase):
    def test_roolin_the_dice_returns_between_1_and_6(self):
        dice = for_numbers.play_dice()
        self.assertGreaterEqual(dice, 1)
        self.assertLessEqual(dice, 6)

    def test_create_a_board_with_24_positions(self):
        board = Board.create_board()
        self.assertEqual(len(board), 24)

    def test_create_a_board_with_20_properties(self):
        board = Board.create_board()
        properties = [i for i, x in board.items() if x["owner"] == ""]
        self.assertEqual(len(properties), 20)

    def test_create_players_with_distinct_behaviors(self):
        players = Players.create_players()
        behaviors = list()
        for _, value in players.items():
            behaviors.append(value["behavior"])

        duplicated = False if len(behaviors) == len(set(behaviors)) else True

        self.assertFalse(duplicated)


if __name__ == "__main__":
    unittest.main(verbosity=2)
