class Solution:
    def maxPower(self, s: str) -> int:
        prev = None
        cnt = 0
        ans = 0
        for c in s:
            if c == prev:
                cnt += 1
            else:
                cnt = 1
                prev = c
            ans = max(ans, cnt)
        return ans
