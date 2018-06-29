from sys import maxsize as maxint


class Solution:
    def minSubArrayLen(self, s, nums):
        cs = 0
        start = 0
        min_len = maxint
        for end in range(len(nums)):
            cs += nums[end]
            while cs >= s and start <= end:
                min_len = min(min_len, end - start + 1)
                if start == end:
                    break
                cs -= nums[start]
                start += 1
        return min_len if min_len != maxint else 0
