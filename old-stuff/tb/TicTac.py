EMPTY = -1
CIRCLE = 0
CROSS = 1

class TicTac:
    def __init__(self, size=3):
        self.size = 3
        self.board = [[EMPTY] * size for _ in range(size)]

    def setCell(self, x, y, val):
        self.board[x][y] = int(val)

    def getCell(self, x, y):
        return self.board[x][y]

    def full(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == EMPTY:
                    return False
        return True

    def print(self):
        cell_map = {-1:'-', 0:'O', 1:'X'}
        fmt_cell = lambda i: cell_map[i]
        fmt_row = lambda r: '|'.join(map(fmt_cell, r))
        print('\n'.join(map(fmt_row, self.board)) + '\n')

class AI:
    def move(self, tt):
        for x in range(tt.size):
            for y in range(tt.size):
                if tt.getCell(x, y) == EMPTY:
                    tt.setCell(x, y, CIRCLE)
                    return
        raise ValueError("board is full, move not possible")

# test1
tt = TicTac()
tt.print()
tt.setCell(1,0, False)
tt.print()
tt.setCell(2,2, True)
tt.print()
ai = AI()
while True:
    try:
        ai.move(tt)
        tt.print()
    except ValueError:
        raise