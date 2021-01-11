class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in reversed(range(n)):
            h, t = s[:(i+1)], s[(i+1):]
            if h == h[::-1]:
                return t[::-1] + s
        return s