#from enum import Enum

class Board:
    cells = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    def insert (self, x, y, player):
        if cells[x, y] == None:
            cells[x,y] = player  

class Player:
    def turn(self, board, x, y):
        board.insert(x,y)

player1 = Player()
player2 = Player()
board = Board()

player1.turn(board.insert(x = 1, y=1,player1), x=1, y=1)

print(Board.cells)