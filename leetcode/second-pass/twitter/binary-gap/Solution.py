from math import inf

class Solution:
    def binaryGap(self, N):
        ans = -inf
        last = -1
        for i in range(32):
            bit = ((1 << i) & N) >> i
            if bit == 1:
                if last >= 0:
                    ans = max(ans, abs(last - i))
                last = i
        return 0 if ans == -inf else ans