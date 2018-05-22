"""
The contribution of a position i-th to the powerset, is formed by those
subsets starting at i+1 that contain nums[i], and those which do not.
"""

class Solution:
    def subsets(self, nums):
        def rec(nums, i, n, curr, powset):
            powset.add(tuple(sorted(curr)))
            if i >= n:
                return
            x = nums[i]
            curr.add(x)
            rec(nums, i+1, n, curr, powset)
            curr.remove(x)
            rec(nums, i+1, n, curr, powset)
        powset = set()
        rec(nums, 0, len(nums), set(), powset)
        return list(powset)