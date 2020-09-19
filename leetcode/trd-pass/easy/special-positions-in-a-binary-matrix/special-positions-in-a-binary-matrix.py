class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row_sum = [0] * n
        col_sum = [0] * m
        for i in range(n):
            for j in range(m):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == row_sum[i] == col_sum[j] == 1:
                    ans += 1
        return ans