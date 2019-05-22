class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        for i in range(32):
            ans += ((1 << i) & n) >> i
        return ans