class Solution:
    def neighbors(self, board, x, y):
        n, m = len(board), len(board[0])
        for dx in (-1, 0, +1):
            for dy in (-1, 0, +1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not (nx == x and ny == y):
                    yield nx, ny

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[
        List[str]]:
        x, y = click
        cell = board[x][y]
        if cell == 'M':
            board[x][y] = 'X'
        elif cell == 'E':
            adjM = sum(
                (board[i][j] == 'M' for i, j in self.neighbors(board, x, y)))
            if adjM == 0:
                board[x][y] = 'B'
                for nei in self.neighbors(board, x, y):
                    self.updateBoard(board, nei)
            else:
                board[x][y] = str(adjM)
        return board
