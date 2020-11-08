from math import factorial as fact

class Solution:
    def comb(self, n, m):
        if n < m:
            return 0
        else:
            return fact(n) // (fact(m) * fact(n - m))

    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        cnt = list(Counter(tiles).values())
        m = len(cnt)
        dp = [[0] * m for _ in range(n + 1)]
        for s in range(1, cnt[0] + 1):
            dp[s][0] = 1
        for i in range(1, m):
            dp[1][i] = dp[1][i-1] + 1
        for s in range(2, n + 1):
            for i in range(1, m):
                dp[s][i] = dp[s][i - 1]
                if cnt[i] >= s:
                    dp[s][i] += 1
                for t in range(1, s):
                    if cnt[i] >= s - t:
                        dp[s][i] += self.comb(s, s - t) * dp[t][i - 1]
        return sum(dp[s][m-1] for s in range(1, n+1))
