class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        start, end = 0, 0
        max_len = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                end = i
            else:
                max_len = max(max_len, end - start  + 1)
                start, end = i, i
        max_len = max(max_len, end - start  + 1)
        return max_len