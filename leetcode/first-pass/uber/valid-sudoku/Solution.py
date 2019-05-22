class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = 9, 3
        row = [[0] * (n + 1) for _ in range(n)]
        col = [[0] * (n + 1) for _ in range(n)]
        blk = [[0] * (n + 1) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                x = int(board[i][j])
                row[i][x] += 1
                col[j][x] += 1
                k = (i // m) * m + j // m
                blk[k][x] += 1
                if row[i][x] > 1 or col[j][x] > 1 or blk[k][x] > 1:
                    return False
        return True
