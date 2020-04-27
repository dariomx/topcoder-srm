from collections import Counter

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros, ones = 0, 0
        diff = dict()
        ans = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeros += 1
            else:
                ones += 1
            d = zeros - ones
            if zeros == ones:
                ans = max(ans, end + 1)
            elif d in diff:
                start = diff[d]
                ans = max(ans, end - start)
            else:
                diff[d] = end
        return ans