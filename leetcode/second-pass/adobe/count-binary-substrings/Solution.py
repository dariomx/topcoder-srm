class Solution:
    def countBinarySubstrings(self, s):
        cnt = [0, 0]
        last = None
        ans = 0
        for bit in s:
            bit = 1 if bit=='1' else 0
            if bit != last:
                cnt[bit] = 0
            cnt[bit] += 1
            other = 1 - bit
            if cnt[other] > 0:
                cnt[other] -= 1
                ans += 1
            last = bit
        return ans