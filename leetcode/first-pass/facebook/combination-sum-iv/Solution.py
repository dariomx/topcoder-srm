class Solution:
    def combinationSum4(self, nums, target):
        cache = dict()

        def rec(s):
            if s > target:
                return 0
            if s in cache:
                return cache[s]
            if s == target:
                ret = 1
            else:
                ret = 0
                for x in nums:
                    ret += rec(s + x)
            cache[s] = ret
            return ret

        return rec(0)
