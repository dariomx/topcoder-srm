# cheated cause needed to copy/adjust the DP solution of partition problem
# which in turn is special case of subset-sum

from collections import Counter


class Solution:
    def partition(self, cnt, k):
        n, K = len(cnt), sum(x for (_, x) in cnt)
        dp = [[None] * (n + 1) for _ in range(K + 1)]
        for j in range(n + 1):
            dp[0][j] = []
        for i in range(1, K + 1):
            for j in range(1, n + 1):
                if dp[i][j - 1] is not None:
                    dp[i][j] = dp[i][j - 1]
                else:
                    x = cnt[j - 1][1]
                    if i - x >= 0 and dp[i - x][j - 1] is not None:
                        dp[i][j] = dp[i - x][j - 1] + [cnt[j - 1]]
        return dp[k][n]

    def interlace(self, ss, cnt):
        left, right = "", ""
        ss = dict(ss)
        for x, k in cnt:
            xs = x * k
            if x in ss:
                left += xs
            else:
                right += xs
        res = "".join(x + y for x, y in zip(left, right))
        if len(left) > len(right):
            res += left[-1]
        return res

    def reorganizeString(self, S: str) -> str:
        cnt = list(Counter(S).items())
        half = len(S) // 2 + len(S) % 2
        ss = self.partition(cnt, half)
        if ss:
            return self.interlace(ss, cnt)
        else:
            return ""
