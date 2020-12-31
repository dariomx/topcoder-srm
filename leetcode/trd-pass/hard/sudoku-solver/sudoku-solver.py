class Solution:
    def getSub(self, x, y):
        return (x // 3) * 3 + (y // 3)

    def search(self, i, pos, board, row, col, sub):
        def setDigit(d):
            board[x][y] = str(d)
            row[x].remove(d)
            col[y].remove(d)
            sub[z].remove(d)

        def unsetDigit(d):
            board[x][y] = '.'
            row[x].add(d)
            col[y].add(d)
            sub[z].add(d)

        if i == len(pos):
            return True
        else:
            x, y = pos[i]
            if board[x][y] != '.':
                return False
            z = self.getSub(x, y)
            for d in row[x] & col[y] & sub[z]:
                setDigit(d)
                if self.search(i + 1, pos, board, row, col, sub):
                    return True
                unsetDigit(d)
            return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        pos = [(x, y) for x in range(n) for y in range(n)]
        row = [set(range(1, n + 1)) for _ in range(n)]
        col = [set(range(1, n + 1)) for _ in range(n)]
        sub = [set(range(1, n + 1)) for _ in range(n)]
        for x in range(n):
            for y in range(n):
                z = self.getSub(x, y)
                d = board[x][y]
                if d != '.':
                    d = int(d)
                    pos.remove((x, y))
                    row[x].discard(d)
                    col[y].discard(d)
                    sub[z].discard(d)
        self.search(0, pos, board, row, col, sub)
