"""
Adapted from

https://leetcode.com/problems/longest-arithmetic-sequence/discuss/415281
/Python-DP-solution

I could not come up with the DP for this ... the missing piece was
to combine the two approaches I was aiming for:

1) Consider the diff somehow

2) DP saving lengths and diff ... but I was saving a single diff, not all!
and this is what prevented me from nailing it down

now ... can we make it backwards as we wanted? yeah, just make sure that you
review the guys in front descendenly, such that you give higher value to
longer sequences (nearest imply longest sub-sequences)

"""


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        n = len(A)
        for i in reversed(range(n - 1)):
            x = A[i]
            for j in reversed(range(i + 1, n)):
                y = A[j]
                diff = x - y
                if (j, diff) in dp:
                    dp[i, diff] = dp[j, diff] + 1
                else:
                    dp[i, diff] = 2
        return max(dp.values())
