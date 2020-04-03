# kinda recall having seen an answer and resurrected from bio-memory

from math import inf

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minx, maxx = inf, -inf
        n = len(nums)
        for i, x in enumerate(nums):
            if x <= 0:
                nums[i] = inf
            else:
                minx = min(minx, x)
                maxx = max(maxx, x)
        if minx > 1:
            return 1
        for i, x in enumerate(nums):
            x = abs(x)
            if x == inf:
                continue
            j = x - minx
            if j < len(nums) and nums[j] > 0:
                nums[j] *= -1
        for i, x in enumerate(nums):
            if x > 0:
                return i + minx
        return maxx + 1