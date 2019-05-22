from math import inf


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [inf] * (n + 1)
        new_dp = [inf] * (n + 1)
        for j in range(n):
            dp[j] = A[n - 1][j]
        for i in range(n - 2, -1, -1):
            for j in range(n):
                new_dp[j] = A[i][j] + min(dp[j - 1], dp[j], dp[j + 1])
            dp, new_dp = new_dp, dp
        return min(dp)

