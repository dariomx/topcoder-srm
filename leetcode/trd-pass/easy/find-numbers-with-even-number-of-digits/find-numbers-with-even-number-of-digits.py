class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if 10 <= x <= 99:
                ans += 1
            elif 1000 <= x <= 9999:
                ans += 1
            elif x == 100000:
                ans += 1
        return ans