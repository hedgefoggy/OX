from enum import Enum

class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2

class Player:
    def __init__(self, cell_type):
        self.cell_type = cell_type


class GameManager:
    """
    Starts all processes.
    """
    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]  # почему приватный ??
        self.current_player = 0
        self.field = GameField()