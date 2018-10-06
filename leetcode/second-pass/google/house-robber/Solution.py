class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            maxp = [0] * n
            maxp[n - 1] = nums[n - 1]
            maxp[n - 2] = max(nums[n - 2], nums[n - 1])
            for i in range(n - 3, -1, -1):
                maxp[i] = max(nums[i] + maxp[i + 2], maxp[i + 1])
            return maxp[0]
