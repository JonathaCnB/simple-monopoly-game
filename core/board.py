from core.property import Property


class Board:
    @staticmethod
    def create_board() -> dict:
        board: dict = dict()
        board[0] = {
            "value": 0,
            "rent": 100,
            "owner": "Bank",
        }

        for i in range(1, 24):
            property = Property(i + 1)
            if i in [6, 12, 18]:
                board[i] = {
                    "value": 0,
                    "rent": 0,
                    "owner": "Bank",
                }
                continue
            board[i] = {
                "value": property.value,
                "rent": property.rent,
                "owner": "",
            }
        return board
