class HorSum:
    def __init__(self, matrix: List[List[int]]):
        self._psum = self._calcPsum(matrix)
        self._matrix = matrix
        
    def _calcPsum(self, matrix: List[List[int]]):        
        m, n = len(matrix), len(matrix[0])
        psum = [[0] * n for _ in range(m)]
        for i in range(m):
            psum[i][0] = matrix[i][0]
            for j in range(1, n):
                psum[i][j] = matrix[i][j] + psum[i][j-1]
        return psum
    
    def sum(self, row:int, start:int, end:int) -> int:
        return self._psum[row][end] - self._psum[row][start] + self._matrix[row][start]

class VerSum:
    def __init__(self, matrix: List[List[int]]):
        self._psum = self._calcPsum(matrix)
        self._matrix = matrix
        
    def _calcPsum(self, matrix: List[List[int]]):        
        m, n = len(matrix), len(matrix[0])
        psum = [[0] * m for _ in range(n)]
        for j in range(n):
            psum[j][0] = matrix[0][j]
            for i in range(1, m):
                psum[j][i] = matrix[i][j] + psum[j][i-1]
        return psum
    
    def sum(self, col:int, start:int, end:int) -> int:
        return self._psum[col][end] - self._psum[col][start] + self._matrix[start][col]    

class Solution:    
    def _countFromDiag(self, x: int, y: int, matrix: List[List[int]]) -> int:
        cnt = 0
        i, j, size = x, y, 1
        m, n = len(matrix), len(matrix[0])
        while i < m and j < n:
            onesx = self._hor.sum(i, y, j)
            onesy = self._ver.sum(j, x, i)
            if size == onesx == onesy:
                cnt += 1
                size += 1
                i += 1
                j += 1
            else:
                break
        return cnt
    
    def countSquares(self, matrix: List[List[int]]) -> int:
        self._hor = HorSum(matrix)
        self._ver = VerSum(matrix)
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 1:
                    ans += self._countFromDiag(x, y, matrix)
        return ans
