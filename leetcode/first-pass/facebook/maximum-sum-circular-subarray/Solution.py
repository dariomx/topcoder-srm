from math import inf

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0
        ans = -inf
        lsum = [0] * n
        min_lsum = inf
        for i in range(n):
            lsum[i] = lsum[i-1] + A[i]
            ans = max(ans, lsum[i], lsum[i] - min_lsum)
            min_lsum = min(min_lsum, lsum[i])
        max_rsum = -inf
        rsum = 0
        for i in range(n-1, 0, -1):
            rsum += A[i]
            max_rsum = max(max_rsum, rsum)
            ans = max(ans, rsum, lsum[i-1] + max_rsum)
        return ans