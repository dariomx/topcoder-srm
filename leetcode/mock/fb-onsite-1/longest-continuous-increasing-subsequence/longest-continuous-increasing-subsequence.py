class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start, last = 0, 0
        ans = 0
        for end in range(len(nums)):
            if nums[last] < nums[end]:
                last = end
            else:
                start = last = end
            ans = max(ans, end - start + 1)
        return ans