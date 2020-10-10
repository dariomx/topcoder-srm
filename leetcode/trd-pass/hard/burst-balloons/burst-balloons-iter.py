# not mine, saw explanation in phorum

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for size in range(1, n-1):
            for i in range(1, n-size):
                j = i + size - 1
                for k in range(i, j+1):
                    c_k = nums[i-1] * nums[k] * nums[j+1]
                    dp[i][j] = max(dp[i][j], c_k + dp[i][k-1] + dp[k+1][j])
        return dp[1][n-2]