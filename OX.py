from enum import Enum


class Board:
    def __init__(self):
        self.cells = [[Cell.VOID,Cell.VOID, Cell.VOID],
                      [Cell.VOID,Cell.VOID, Cell.VOID],
                      [Cell.VOID,Cell.VOID, Cell.VOID]]


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    def __init__(self, player,cell_type):
        self.cell_type = Cell(Enum)
        self.player = player

    def get_icon (self):
        return  player.cell_type

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = Player()
        self.player1 = Player()

        self.current_player = 0
        self.board = Board()

