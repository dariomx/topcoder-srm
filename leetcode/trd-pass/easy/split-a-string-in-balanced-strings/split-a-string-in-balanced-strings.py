class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        ans = 0
        for end, c in enumerate(s):
            if c == 'L':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans