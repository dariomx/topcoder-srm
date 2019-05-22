# stolen from https://en.wikipedia.org/wiki/Partition_problem#The_pseudo
# -polynomial_algorithm

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 == 1:
            return False
        n, half = len(nums), S // 2
        dp = [[False] * (n + 1) for _ in range(half + 1)]
        for i in range(n + 1):
            dp[0][i] = True
        for i in range(1, half + 1):
            for j in range(1, n + 1):
                si = i - nums[j - 1]
                if si >= 0:
                    dp[i][j] = dp[i][j - 1] or dp[si][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[half][n]
