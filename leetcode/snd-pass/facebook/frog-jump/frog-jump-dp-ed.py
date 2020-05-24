# python port of the iterative dp editorial solution (kinda similiar to
# my recursive version)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = {i: set() for i in stones}
        dp[stones[0]].add(0)
        for i in stones:
            for k in dp[i]:
                for nk in (k - 1, k, k + 1):
                    ni = i + nk
                    if ni > i and ni in dp:
                        dp[ni].add(nk)
        return len(dp[stones[n - 1]]) > 0
