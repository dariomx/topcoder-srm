class Solution(object):
    def titleToNumber(self, s):
        k = 26
        pow_k = 1
        ans = 0
        for c in reversed(s):
            ans += pow_k * (ord(c) - ord('A') + 1)
            pow_k *= k
        return ans