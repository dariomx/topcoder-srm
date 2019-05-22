from sys import maxsize as maxint


class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n == 0:
            return 0
        sum = nums[0]
        start, end = 0, 0
        min_len = maxint
        while True:
            if sum < s:
                if end + 1 < n:
                    end += 1
                    sum += nums[end]
                else:
                    break
            elif sum > s:
                min_len = min(min_len, end - start + 1)
                if start + 1 <= end:
                    sum -= nums[start]
                    start += 1
                else:
                    break
            else:
                min_len = min(min_len, end - start + 1)
                if end + 1 < n:
                    end += 1
                    sum += nums[end]
                elif start + 1 <= end:
                    sum -= nums[start]
                    start += 1
                else:
                    break
        return 0 if min_len == maxint else min_len

