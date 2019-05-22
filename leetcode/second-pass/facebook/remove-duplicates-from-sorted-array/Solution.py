class Solution:
    def removeDuplicates(self, nums):
        i = 0
        prev = None
        for j in range(len(nums)):
            if nums[j] != prev:
                nums[i] = nums[j]
                i += 1
                prev = nums[j]
        return i