class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        swaps = 1
        while swaps > 0:
            swaps = 0
            for i in range(n):
                x = nums[i]
                if x <= 0:
                    continue
                else:
                    x -= 1
                if nums[x] >= 0:
                    nums[i], nums[x] = nums[x], -1
                    swaps += 1
                else:
                    nums[i] = 0
        return [i + 1 for i in range(n) if nums[i] == 0]

