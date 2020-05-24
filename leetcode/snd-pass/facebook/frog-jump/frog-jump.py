# dp[i][k] = if you can reach i-th stone by jumping k, you can make it
#
# not even sure why this one works, as im just caring about considering
# the exact distances with the stones ahead, should not i consider as
# well the cases dp[i][k-1] and dp[i][k+1]? does this pass due lack of
# more generic test-cases?

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [defaultdict(lambda: False) for _ in range(n)]
        dp[n-1] = defaultdict(lambda: True)
        for i in reversed(range(n-1)):
            for j in range(i+1, n):
                k = stones[j] - stones[i]
                dp[i][k] = dp[j][k] or dp[j][k+1] or dp[j][k-1]
        return dp[0][1]