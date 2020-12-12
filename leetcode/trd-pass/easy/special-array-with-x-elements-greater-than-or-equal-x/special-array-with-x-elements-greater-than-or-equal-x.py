class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        lbound = -1
        for i, y in enumerate(nums):
            x = n - i
            if y >= x and x > lbound:
                return x
            else:
                lbound = y
        return -1