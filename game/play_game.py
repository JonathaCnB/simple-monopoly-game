from core.behaviors import Behaviors
from core.board import Board
from core.players import Players
from ultils.for_numbers import play_dice


class Game:
    def __init__(self) -> None:
        self.board = Board.create_board()
        self.players = Players.create_players()
        self.turn: int = 0
        self.position_players: dict = dict()
        self.queue: int = 0
        self.total_active_players = len(self.players)
        self.total_turns_played: int = 0
        self.player_victory: int = 0
        self.for_time_out: int = 0
        self.winning_behavior: dict = dict()

    def random_players(self) -> dict:
        randomized_players = Players.random_players(self.players)
        return randomized_players

    @staticmethod
    def buy(player: dict, property_value: int, property_rent: int) -> bool:
        behavior = Behaviors(property_value, property_rent, player["balance"])
        for callable in Behaviors.__dict__.values():
            if hasattr(callable, "__call__"):
                if callable.__name__ == player["behavior"]:
                    return callable(behavior)
        return False

    def position_control(self, now: int, player: dict, dice: int) -> None:
        for key, _ in self.position_players.items():
            if key == now:
                if self.position_players[now]["position"] == "Game Over":
                    return

                next_position = self.position_players[key]["position"] + dice

                if next_position > len(self.board):
                    self.position_players[key]["balance"] += 100
                    next_position %= len(self.board) + 1
                self.position_players[key]["position"] = next_position

                return self.position_players[key]["position"]

        self.position_players.update(
            {
                now: {
                    "behavior": player["behavior"],
                    "balance": player["balance"],
                    "position": dice,
                },
            }
        )
        return self.position_players[now]["position"]

    def player_turn_control(self) -> int:
        qty_players = len(self.players)
        now = self.queue + 1 if self.queue < qty_players else 1
        self.queue = now
        return now

    def control_properties(
        self,
        now: int,
        position: int,
        player: dict,
    ) -> None:
        board = self.board
        play_now = self.position_players[now]
        for key, value in board.items():
            if key == position:
                value_owner = value["owner"]
                property_value = value["value"]
                property_rent = value["rent"]

                if value_owner == "Bank" or value_owner == now:
                    return
                if value_owner and value_owner != "Bank":
                    play_owner = self.position_players[value_owner]
                    if play_now["balance"] < property_rent:
                        play_owner["balance"] += play_now["balance"]
                        play_now["balance"] = 0
                        self.bankrupt(now)
                        return
                    play_now["balance"] -= property_rent
                    play_owner["balance"] += property_rent
                    return

                if play_now["balance"] < property_value:
                    return

                can_buy = self.buy(player, property_value, property_rent)

                if can_buy:
                    value["owner"] = now
                    play_now["balance"] -= property_value
                    return
        return

    def bankrupt(self, now: int) -> None:
        board = self.board
        for _, value in board.items():
            if value["owner"] == now:
                value["owner"] = ""
        self.position_players[now]["position"] = "Game Over"
        self.total_active_players -= 1
        return

    def new_roud(self) -> None:
        self.position_players.clear()
        self.turn = 0
        self.total_active_players = len(self.players)
        self.board = Board.create_board()

    def processes_data(self, total_simulations: int) -> None:
        wins: int = 0
        behavior_more_wins: str
        shift_average = self.total_turns_played / total_simulations
        for key, value in self.winning_behavior.items():
            if value > wins:
                behavior_more_wins = key
            percent = (value * 100) / self.player_victory
            self.winning_behavior[key] = {
                "qty_wins": value,
                "percent": f"{round(percent,2)}%",
            }
        collection_result(
            turn=shift_average,
            behavior=self.winning_behavior,
            time_out=self.for_time_out,
            behavior_more_wins=behavior_more_wins,
        )


def play_game():
    game = Game()
    players = game.random_players()
    i = 0
    simulation = 0
    round = 1000
    total_simulations = 100
    while i < round:
        game.turn += 1
        now = game.player_turn_control()
        dice = play_dice()
        position = game.position_control(now, players[now], dice)
        game.control_properties(now, position, players[now])
        if game.total_active_players == 1:
            for key, value in game.position_players.items():
                if value["position"] != "Game Over":
                    behavior = game.position_players[key]["behavior"]
            game.player_victory += 1
            game.total_turns_played += game.turn
            try:
                game.winning_behavior[behavior] += 1
            except KeyError:
                game.winning_behavior.update({behavior: 1})

            simulation += 1
            if simulation == total_simulations:
                game.processes_data(total_simulations)
                break
            game.new_roud()
            players = game.random_players()
            i = 0
            continue
        i += 1
        if i == 1000:
            game.total_turns_played += game.turn
            game.for_time_out += 1
            game.new_roud()
            players = game.random_players()
            simulation += 1
            if simulation == total_simulations:
                game.processes_data(total_simulations)
                break
            i = 0
            continue


def collection_result(*args, **kwargs):
    time_out = kwargs.get("time_out")
    avg_turn = kwargs.get("turn")
    behaviors = kwargs.get("behavior")
    behavior_more_wins = kwargs.get("behavior_more_wins")
    print("#" * 15, "Conclusion", "#" * 15)
    print(f"\tQuantas partidas terminam por time out - {time_out}")
    print(f"\tQuantos turnos em média demora uma partida - {avg_turn}")
    print(
        "\tQual a porcentagem de vitórias por comportamento dos jogadores - "
        f"{behaviors}"
    )
    print(f"\tQual o comportamento que mais vence - {behavior_more_wins}")
    print("::" * 10, "Fineshed")
