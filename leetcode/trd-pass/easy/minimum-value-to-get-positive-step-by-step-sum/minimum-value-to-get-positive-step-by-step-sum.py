from math import inf

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        psum = 0
        ans = -inf
        for x in nums:
            psum += x
            ans = max(ans, -psum + 1)
        return max(1, ans)