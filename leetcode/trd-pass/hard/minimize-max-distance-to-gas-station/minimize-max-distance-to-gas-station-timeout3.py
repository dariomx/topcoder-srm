from sortedcontainers import SortedList


class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        dist = [stations[i] - stations[i - 1] for i in range(1, len(stations))]
        N = len(dist)
        dp = [[inf] * (K + 1) for _ in range(N)]
        for j in range(K + 1):
            dp[N - 1][j] = dist[N - 1] / (j + 1)
        for i in reversed(range(N - 1)):
            for j in range(K + 1):
                dist_j = dist[i] / (j + 1)
                for k in range(K + 1):
                    if j + k > K:
                        continue
                    dp[i][j + k] = min(dp[i][j + k], max(dist_j, dp[i + 1][k]))
        return dp[0][K]
