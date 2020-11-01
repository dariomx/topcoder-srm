from operator import lt, gt


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for cmp in (lt, gt):
            dp = [[0] * 4 for _ in range(n)]
            for i in range(n):
                dp[i][1] = 1
            for k in (2, 3):
                for i in range(n):
                    for j in range(i + 1, n):
                        if cmp(rating[i], rating[j]):
                            dp[i][k] += dp[j][k - 1]
                    ans += dp[i][3]
        return ans

