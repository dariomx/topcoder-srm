class Solution:
    def findRook(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return i, j

    def searchPawn(self, board, i, j, di, dj):
        while 0 < i < 8 and 0 < j < 8:
            if board[i][j] == 'p':
                return 1
            elif board[i][j] == 'B':
                return 0
            i += di
            j += dj
        return 0

    def numRookCaptures(self, board: List[List[str]]) -> int:
        i, j = self.findRook(board)
        ans = 0
        for di, dj in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
            ans += self.searchPawn(board, i, j, di, dj)
        return ans 