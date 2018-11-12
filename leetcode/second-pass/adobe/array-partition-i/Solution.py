class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += min(nums[i], nums[i+1])
        return ans