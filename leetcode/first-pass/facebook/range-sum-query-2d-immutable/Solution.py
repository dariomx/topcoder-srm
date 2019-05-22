class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.csum = None
        n = len(matrix)
        if n > 0:
            m = len(matrix[0])
        else:
            return
        csum = [[0] * m for _ in range(n)]
        csum[0][0] = matrix[0][0]
        for j in range(1, m):
            csum[0][j] = csum[0][j - 1] + matrix[0][j]
        for i in range(1, n):
            psum = 0
            for j in range(m):
                psum += matrix[i][j]
                csum[i][j] = csum[i - 1][j] + psum
        self.csum = csum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.csum:
            return 0
        ans = self.csum[row2][col2]
        if row1 > 0:
            ans -= self.csum[row1 - 1][col2]
        if col1 > 0:
            ans -= self.csum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            ans += self.csum[row1 - 1][col1 - 1]
        return ans
