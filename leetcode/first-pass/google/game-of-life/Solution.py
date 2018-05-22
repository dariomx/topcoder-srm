class Solution(object):
    def encodeCell(self, oldCell, newCell):
        if newCell == oldCell:
            return newCell
        elif oldCell == 0 and newCell == 1:
            return -1
        else:
            return -2

    def decodeOldCell(self, encCell):
        if encCell >= 0:
            return encCell
        elif encCell == -1:
            return 0
        else:
            return 1

    def decodeNewCell(self, encCell):
        if encCell >= 0:
            return encCell
        elif encCell == -1:
            return 1
        else:
            return 0

    def countAliveNeighbors(self, x, y, board):
        cnt = 0
        m, n = len(board), len(board[0])
        for i in xrange(x - 1, x + 2):
            for j in xrange(y - 1, y + 2):
                if 0 <= i < m and 0 <= j < n and (i, j) != (x, y):
                    cnt += self.decodeOldCell(board[i][j])
        return cnt

    def calcNewCell(self, oldCell, aliveN):
        if (oldCell == 1 and (aliveN in (2, 3))) or \
                (oldCell == 0 and aliveN == 3):
            return 1
        else:
            return 0

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for x in xrange(m):
            for y in xrange(n):
                oldCell = board[x][y]
                aliveN = self.countAliveNeighbors(x, y, board)
                newCell = self.calcNewCell(oldCell, aliveN)
                board[x][y] = self.encodeCell(oldCell, newCell)
        for x in xrange(m):
            for y in xrange(n):
                board[x][y] = self.decodeNewCell(board[x][y])


board = [[1, 1], [1, 0]]
Solution().gameOfLife(board)
print(board)
