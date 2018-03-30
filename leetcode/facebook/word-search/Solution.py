class Solution:
    def search(self, board, start, path, word, used):
        x, y = start
        if path == word:
            return True
        if len(path) >= len(word):
            return False
        n, m = len(board), len(board[0])
        for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i < n and 0 <= j < m and (i, j) not in used:
                c = board[i][j]
                if c != word[len(path)]:
                    continue
                used.add((i, j))
                if self.search(board, (i, j), path + c, word, used):
                    return True
                used.remove((i, j))
        return False

    def exist(self, board, word):
        n = len(board)
        if n == 0:
            return False
        m = len(board[0])
        if m == 0:
            return False
        used = set()
        for x in range(n):
            for y in range(m):
                if board[x][y] != word[0]:
                    continue
                used.clear()
                used.add((x, y))
                if self.search(board, (x, y), board[x][y], word, used):
                    return True
                used.remove((x, y))
        return False

