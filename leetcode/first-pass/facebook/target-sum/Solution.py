class Solution:
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        cache = dict()

        def rec(i, s):
            if (i, s) in cache:
                return cache[(i, s)]
            if i == n:
                if s == target:
                    ret = 1
                else:
                    ret = 0
            else:
                ret = rec(i + 1, s + nums[i]) + rec(i + 1, s - nums[i])
            cache[(i, s)] = ret
            return ret

        return rec(0, 0)
