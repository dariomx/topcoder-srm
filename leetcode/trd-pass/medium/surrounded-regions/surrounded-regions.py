class Solution:
    def dfs(self, start, board):
        n, m = len(board), len(board[0])
        stack = list(start)
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            x, y = node
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                elif board[nx][ny] == 'O':
                    stack.append((nx, ny))
        return visited

    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        start = []
        for x in range(n):
            for y in range(m):
                if (x in (0, n - 1) or y in (0, m - 1)) and board[x][y] == 'O':
                    start.append((x, y))
        visited = self.dfs(start, board)
        for x in range(n):
            for y in range(m):
                if board[x][y] == 'O' and (x, y) not in visited:
                    board[x][y] = 'X'


