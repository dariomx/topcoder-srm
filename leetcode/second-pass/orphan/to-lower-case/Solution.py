class Solution:
    def toLowerCase(self, str):
        ans = ""
        delta = ord('a') - ord('A')
        for c in str:
            i = ord(c)
            if ord('A') <= i <= ord('Z'):
                ans += chr(i + delta)
            else:
                ans += c
        return ans

