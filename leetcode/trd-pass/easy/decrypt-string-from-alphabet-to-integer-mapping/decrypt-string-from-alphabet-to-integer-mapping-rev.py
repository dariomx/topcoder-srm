# easier than mine, just proc in reverse order (instead of deque i used)
# mmm, though they iterate twice (for reversing answer)

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        ans = ''
        while i >= 0:
            if s[i] == '#':
                x = s[i - 1]
                y = s[i - 2]
                dd = chr(ord('j') + int(y + x) - 10)
                ans += dd
                i -= 3
            else:
                d = chr(ord('a') + int(s[i]) - 1)
                ans += d
                i -= 1
        return ans[::-1]
