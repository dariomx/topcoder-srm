class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for x in (2*i + 1 for i in range(n)):
            if x < n:
                ans += n - x
            else:
                break
        return ans