class Solution:
    def splitArray(self, nums, m):
        n = len(nums)
        if n == 0:
            return 0
        max_sum = [[None] * (m + 1) for _ in range(n)]
        left_sum = [[None] * (m + 1) for _ in range(n)]
        cum_sum = [0] * n
        max_sum[n - 1][1] = nums[n - 1]
        left_sum[n - 1][1] = nums[n - 1]
        cum_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            cum_sum[i] = cum_sum[i + 1] + nums[i]
            max_sum[i][1] = cum_sum[i]
            left_sum[i][1] = cum_sum[i]
            for k in range(2, m + 1):
                if max_sum[i + 1][k]:
                    left_sum[i][k] = left_sum[i + 1][k] + nums[i]
                    max_sum[i][k] = max(max_sum[i + 1][k], left_sum[i][k])
                for j in range(i + 1, n):
                    if not max_sum[j][k - 1]:
                        continue
                    left = cum_sum[i] - cum_sum[j]
                    s_max_sum = max(max_sum[j][k - 1], left)
                    if not max_sum[i][k] or s_max_sum < max_sum[i][k]:
                        left_sum[i][k] = left
                        max_sum[i][k] = s_max_sum
        return max_sum[0][m]
