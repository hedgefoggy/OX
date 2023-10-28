class Board:
    size = 3
    cells = [' ' for _ in range(size*size)]

    def print_board(self):
        #print(id(self))
        size = self.size
        print("-------")
        for cell in range(size):
            print("|",end="")
            for column in range(size):
                print(self.cells[cell * size + column],end ="|")
            print("\n-------")

    def insert(self, player, cell):
        self.cells[cell]
        #self.print_board()
        print()
        if cell != "":
            print("Cell is occupied!")
            print()
        else:
            cell = player.badge


class Player:
    badge = ""

    def turn(self, board, cell):
        board.insert(self,cell)


player1 = Player()
player2 = Player()
board = Board()

player1.badge = 'X'
player2.badge = 'O'



while True:
    board.print_board()
    player1.turn(board, int(input("X select cell: ")))
    board.print_board()
    player2.turn(board, int(input("O select cell: ")))


