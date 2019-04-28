from math import inf

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[inf]*(n+1) for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = A[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(n):
                dp[i][j] = A[i][j] + \
                    min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
        return min(dp[0])