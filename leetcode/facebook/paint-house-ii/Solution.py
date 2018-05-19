from sys import maxsize as maxint


class Solution:
    def minCostII(self, costs):
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        mcost = [[maxint] * k for _ in range(n)]
        for j in range(k):
            mcost[n - 1][j] = costs[n - 1][j]
        for i in range(n - 2, -1, -1):
            for j in range(k):
                for l in range(k):
                    if j == l:
                        continue
                    mcost[i][j] = min(mcost[i][j],
                                      costs[i][j] + mcost[i + 1][l])
        return min(mcost[0])

