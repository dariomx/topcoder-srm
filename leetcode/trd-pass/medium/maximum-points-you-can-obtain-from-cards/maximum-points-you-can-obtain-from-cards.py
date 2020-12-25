class Solution:
    def maxScore(self, P: List[int], k: int) -> int:
        S = sum(P[-k:])
        n = len(P)
        ans = S
        for i in range(k):
            S += P[i] - P[n - k + i]
            ans = max(ans, S)
        return ans
