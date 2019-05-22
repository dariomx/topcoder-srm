class Solution:
    def numDecodings(self, s):
        n = len(s)
        nums = list(map(int, s))
        cache = dict()
        def rec(i):
            if i in cache:
                return cache[i]
            if i == n:
                ans = 1
            else:
                ans = 0
                if nums[i] > 0:
                    ans += rec(i+1)
                if i < n-1 and 10 <= nums[i]*10 + nums[i+1] <= 26:
                    ans += rec(i+2)
            cache[i] = ans
            return ans
        return rec(0)
