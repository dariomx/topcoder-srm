class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0
        n = len(nums)
        while start < n and nums[start] != 0:
            start += 1
        end = start + 1
        while True:
            while end < n and nums[end] == 0:
                end += 1
            if end < n:
                nums[start] = nums[end]
                nums[end] = 0
                start += 1
                end += 1
            else:
                break