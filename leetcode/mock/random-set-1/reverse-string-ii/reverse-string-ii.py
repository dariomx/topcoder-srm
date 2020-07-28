class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        i, n = 0, len(s)
        while i < n:
            ans += s[i:i+k][::-1] + s[i+k:i+2*k]
            i += 2 * k
        return ans