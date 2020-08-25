class Solution:
    def _same_line(self, board, x, y, dx, dy):
        k = self.k
        sym = board[x][y]
        ix, iy = x, y
        for _ in range(k):
            if board[x][y] != sym:
                print(sym, ix, iy, dx, dy, x, y)
                return False
            else:
                x = (x + dx) % k
                y = (y + dy) % k
        return True

    def _has_won(self, board, x, y):
        return self._same_line(board, x, y, 0, 1) or \
               self._same_line(board, x, y, 1, 0) or \
               (x == y and self._same_line(board, x, y, 1, 1)) or \
               (x + y == self.k - 1 and self._same_line(board, x, y, -1, 1))

    def tictactoe(self, moves: List[List[int]], k=3) -> str:
        self.k = k
        board = [[""] * k for _ in range(k)]
        sym = {"A": "X", "B": "O"}
        player = "A"
        for x, y in moves:
            board[x][y] = sym[player]
            if self._has_won(board, x, y):
                return player
            if player == "A":
                player = "B"
            else:
                player = "A"
        if len(moves) < k ** 2:
            return "Pending"
        else:
            return "Draw"