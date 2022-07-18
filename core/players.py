import random

from core.behaviors import Behaviors


class Players:
    @staticmethod
    def create_players() -> dict:
        players: dict = dict()
        index = 0
        for param in Behaviors.__dict__.values():
            if hasattr(param, "__call__"):
                if not param.__name__ == "__init__":
                    behavior = param.__name__
                    index += 1
                    players[index] = {"behavior": behavior, "balance": 300}

        return players

    @staticmethod
    def random_players(players: dict) -> dict:
        player_values = list(players.keys())
        position = 0
        random.shuffle(player_values)
        randomized_players = dict()

        for key in player_values:
            position += 1
            randomized_players.update({position: players[key]})

        return randomized_players
