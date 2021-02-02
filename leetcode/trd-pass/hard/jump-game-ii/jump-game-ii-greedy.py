# my adaptation of the best greedy I found: https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!

# see the discussion in thread above, I posted there several variants to
# converge to this version

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        start, end = 0, nums[0]
        ans = 1
        while end < n - 1:
            ans += 1
            start, end = end, max(i + nums[i] for i in range(start, end+1))
        return ans