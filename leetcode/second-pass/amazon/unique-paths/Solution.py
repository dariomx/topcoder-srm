class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [0] * (n + 1)
        prev = [0] * (n + 1)
        prev[0] = 1
        for i in range(m):
            for j in range(n):
                curr[j] = curr[j - 1] + prev[j]
            curr, prev = prev, curr
        return prev[n - 1]



