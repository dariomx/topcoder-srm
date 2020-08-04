class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0] * 2 * (max(A) - min(A)) for _ in range(n)]
        dp[1][A[1] - A[0]] = 2
        ans = 2
        for i in range(2, n):
            x = A[i]
            for j in range(i):
                k = x - A[j]
                dp[i][k] = max(2, 1 + dp[j][k])
                ans = max(ans, dp[i][k])
        return ans
