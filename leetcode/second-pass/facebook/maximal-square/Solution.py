class Solution:
    def maximalSquare(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        max_area = 0
        rec = [[int(matrix[i][j]) for j in range(m)] for i in range(n)]
        for j in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                if rec[i][j] == 0:
                    continue
                down = rec[i + 1][j] if i != n - 1 else 0
                right = rec[i][j + 1] if j != m - 1 else 0
                diag = rec[i + 1][j + 1] if i != n - 1 and j != m - 1 else 0
                rec[i][j] = 1 + min(down, right, diag)
                max_area = max(max_area, rec[i][j] ** 2)
        return max_area

