from math import inf

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [triangle[0][0]]
        for i in range(1, n):
            m = len(triangle[i])
            new_dp = [0] * m
            for j in range(m):
                left, right = inf, inf
                if j-1 >= 0:
                    left = dp[j-1]
                if j < len(dp):
                    right = dp[j]
                new_dp[j] = triangle[i][j] + min(left, right)
            dp = new_dp
        return min(dp)
