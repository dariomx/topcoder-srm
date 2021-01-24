class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[inf] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(0, -dungeon[m - 1][n - 1])
        for i in reversed(range(m - 1)):
            dp[i][n - 1] = max(0, -(dungeon[i][n - 1] - dp[i + 1][n - 1]))
        for j in reversed(range(n - 1)):
            dp[m - 1][j] = max(0, -(dungeon[m - 1][j] - dp[m - 1][j + 1]))
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                dp[i][j] = max(0, -(
                            dungeon[i][j] - min(dp[i + 1][j], dp[i][j + 1])))
        return dp[0][0] + 1
