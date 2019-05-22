from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                k = bisect_left(nums, nums[i] + nums[j])
                ans += max(0, k - 1 - j)
        return ans