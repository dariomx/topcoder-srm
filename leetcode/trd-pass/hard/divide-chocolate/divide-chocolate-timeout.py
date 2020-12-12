# This times out but in my favor, I did not use the unstated assumption
# that the sweetness array was sorted; which seems to derive somehow
# that the segment we get needs to lie on the left side.

class RangeSum:
    def __init__(self, A):
        n = len(A)
        psum = [0] * n
        psum[0] = A[0]
        for i in range(1, n):
            psum[i] = psum[i - 1] + A[i]
        self.psum = psum
        self.A = A

    def get(self, start, end):
        return self.psum[end] - self.psum[start] + self.A[start]


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        N, S = len(sweetness), sum(sweetness)
        dp = [[-inf] * N for _ in range(K + 2)]
        rsum = RangeSum(sweetness)
        for j in reversed(range(N)):
            dp[1][j] = rsum.get(j, N - 1)
        for i in range(2, K + 2):
            for j in reversed(range(N)):
                if N - j - 1 < i - 1:
                    dp[i][j] = inf
                    continue
                for l in range(j, N - 1):
                    if dp[i - 1][l + 1] != inf:
                        dp[i][j] = max(dp[i][j],
                                       min(rsum.get(j, l), dp[i - 1][l + 1]))
        return max(x for x in dp[K + 1] if abs(x) != inf)
