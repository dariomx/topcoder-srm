from collections import defaultdict


class TicTacToe:
    def __init__(self, n: int, n_players=2):
        self.n = n
        self.cnt_rows = [[0] * n for _ in range(n_players + 1)]
        self.cnt_cols = [[0] * n for _ in range(n_players + 1)]
        self.cnt_diag = [[0] * n for _ in range(n_players + 1)]

    def move(self, row: int, col: int, player: int) -> int:
        self.cnt_rows[player][row] += 1
        if self.cnt_rows[player][row] == self.n:
            return player
        self.cnt_cols[player][col] += 1
        if self.cnt_cols[player][col] == self.n:
            return player
        if row == col:
            self.cnt_diag[player][0] += 1
            if self.cnt_diag[player][0] == self.n:
                return player
        if row + col == self.n - 1:
            self.cnt_diag[player][1] += 1
            if self.cnt_diag[player][1] == self.n:
                return player
        return 0
