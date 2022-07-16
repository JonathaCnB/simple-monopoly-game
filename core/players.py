from core.behaviors import Behaviors


class Players:
    @staticmethod
    def create_players() -> dict:
        players: dict = dict()
        index = 0
        for param in Behaviors.__dict__.values():
            if hasattr(param, "__call__"):
                behavior = param.__name__
                index += 1
                players[index] = {"behavior": behavior, "balance": 300}

        return players
