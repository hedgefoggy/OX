#from enum import Enum

class Board:
    def __init__(self, cells):
        self.cells = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    def insert (self, player,x, y):
        if cells[x, y] == None:
            cells[x,y] = player  


class Player:
    def turn(self, board, x, y):
        board.insert(x,y)


player1 = Player()
player2 = Player()
board = Board()


print()