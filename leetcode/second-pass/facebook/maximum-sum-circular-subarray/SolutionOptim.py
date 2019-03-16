# single-pass possible thanks to duality found in lee215 solution
from math import inf

class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        ans = -inf
        ans_dual = inf
        min_psum = inf
        max_psum = -inf
        psum = 0
        for x in A:
            psum += x
            ans = max(ans, psum, psum - min_psum)
            ans_dual = min(ans_dual, psum - max_psum)
            min_psum = min(min_psum, psum)
            max_psum = max(max_psum, psum)
        return max(ans, psum - ans_dual)

A = [-3, -1, -2]
print(Solution().maxSubarraySumCircular(A))