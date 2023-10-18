from enum import Enum
class Board:
    cells = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    def insert (self, player,x, y):
        if self.cells[x][y] != None:
            print("Cell is occupied")
        else:
            self.cells[x][y] = player


class Player:

    badge = ""

    def turn(self, board, x, y):
        board.insert(self,x,y)


player1 = Player()
player2 = Player()
board = Board()

player1.turn(board,1,1)


print(board.cells)
