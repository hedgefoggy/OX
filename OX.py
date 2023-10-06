class Board:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2