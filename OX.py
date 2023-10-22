class Board:
    cells = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

    def print_board(self):
            for cell in board.cells:
                print(cell)

    def insert (self, player,x, y):
        self.print_board()
        print()
        if self.cells[x][y] != "":
            print("Cell is occupied!")
            print()
        else:
            self.cells[x][y] = player.badge


class Player:

    badge = ""

    def turn(self, board, x, y):
        board.insert(self,x,y)


player1 = Player()
player2 = Player()
board = Board()

player1.badge = "X"
player1.turn(board,1,1)

player2.badge = "O"
player2.turn(board,2,2)

player1.badge = "X"
player1.turn(board,1,1)

board.print_board()
