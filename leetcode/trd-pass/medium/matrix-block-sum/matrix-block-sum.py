class Solution:
    def refSum(self, mat):
        m, n = len(mat), len(mat[0])
        ret = [[0] * n for _ in range(m)]
        for i in range(m):
            psum = 0
            for j in range(n):
                psum += mat[i][j]
                ret[i][j] = psum + ret[i - 1][j]
        return ret

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        R = self.refSum(mat)
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            r1, r2 = max(0, i - K), min(m - 1, i + K)
            for j in range(n):
                c1, c2 = max(0, j - K), min(n - 1, j + K)
                ans[i][j] = R[r2][c2]
                if r1 - 1 >= 0:
                    ans[i][j] -= R[r1 - 1][c2]
                if c1 - 1 >= 0:
                    ans[i][j] -= R[r2][c1 - 1]
                if r1 - 1 >= 0 and c1 - 1 >= 0:
                    ans[i][j] += R[r1 - 1][c1 - 1]
        return ans