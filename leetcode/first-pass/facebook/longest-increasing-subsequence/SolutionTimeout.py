class Solution:
    def lengthOfLIS(self, nums):
        def rec(end, last, size):
            key = (end, last, size)
            if key in cache:
                return cache[key]
            if end == len(nums):
                ret = size
            elif last < nums[end]:
                ret = max(rec(end + 1, nums[end], size + 1),
                          rec(end + 1, last, size))
            else:
                ret = max(rec(end + 1, nums[end], 1),
                          rec(end + 1, last, size))
            ret = max(cache.get(key, 0), ret)
            cache[key] = ret
            return cache[key]

        if not nums:
            return 0
        else:
            cache = dict()
            return rec(0, nums[0], 1)

