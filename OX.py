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
