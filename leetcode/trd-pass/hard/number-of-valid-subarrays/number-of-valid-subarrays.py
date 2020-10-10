class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for x in reversed(nums):
            size = 1
            while stack and x <= stack[-1][0]:
                size += stack.pop()[1]
            stack.append((x, size))
            ans += size
        return ans

