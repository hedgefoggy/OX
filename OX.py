class Board:
    cells = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

    def print_board(self):
        for cell in board.cells:
            print(cell)

    def insert(self, player, x, y):
        self.print_board()
        print()
        if self.cells[x][y] != "":
            print("Cell is occupied!")
            print()
        else:
            self.cells[x][y] = player.badge

    def check_winner(self, player):
        if (
            self.cells[0][0] == player.badge and self.cells[0][1] == player.badge and self.cells[0][2] == player.badge or \
            self.cells[0][0] == player.badge and self.cells[1][1] == player.badge and self.cells[2][2] == player.badge or \
            self.cells[1][0] == player.badge and self.cells[1][1] == player.badge and self.cells[1][2] == player.badge or \
            self.cells[2][0] == player.badge and self.cells[2][1] == player.badge and self.cells[2][2] == player.badge or \
            self.cells[0][1] == player.badge and self.cells[1][1] == player.badge and self.cells[2][1] == player.badge or \
            self.cells[0][2] == player.badge and self.cells[1][2] == player.badge and self.cells[2][2] == player.badge or \
            self.cells[0][0] == player.badge and self.cells[1][0] == player.badge and self.cells[2][0] == player.badge or \
            self.cells[0][2] == player.badge and self.cells[1][1] == player.badge and self.cells[2][0] == player.badge):
            print("Winner is: ", player.badge)


class Player:
    badge = ""

    def turn(self, board, x, y):
        board.insert(self, x, y)


player1 = Player()
player2 = Player()
board = Board()

player1.badge = "X"
player1.turn(board, 0, 0)

player1.badge = "X"
player1.turn(board, 0, 1)

player1.badge = "X"
player1.turn(board, 0, 2)

board.print_board()
board.check_winner(player1)
