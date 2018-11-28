from math import inf


class Solution:
    def dominantIndex(self, nums):
        dom_ix = None
        dom = -inf
        for i in range(len(nums)):
            if nums[i] > dom:
                dom_ix = i
                dom = nums[dom_ix]
        for x in nums:
            if x != dom and dom < 2 * x:
                return -1
        return dom_ix

