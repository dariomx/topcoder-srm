from math import inf


class Solution:
    def maxSubArray(self, nums):
        psum, min_psum, ans = 0, inf, -inf
        for i in range(len(nums)):
            psum += nums[i]
            ans = max(ans, psum - min_psum, psum)
            min_psum = min(min_psum, psum)
        return ans
