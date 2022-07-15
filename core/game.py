from core.property import Property


class Game:
    @staticmethod
    def create_board():
        board = []
        board.clear()
        for i in range(0, 20):
            property = Property(i + 1)
            board.append(
                {
                    "position": property.position,
                    "value": property.value,
                    "rent": property.rent,
                    "owner": "",
                }
            )
        return board
