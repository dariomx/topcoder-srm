class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        start, end = min(startTime), max(endTime)
        n = end + 2
        tasks = [[] for _ in range(n)]
        for i in range(len(startTime)):
            tasks[startTime[i]].append(i)
        dp = [0] * n
        for t in reversed(range(start, end + 1)):
            dp[t] = dp[t + 1]
            for i in tasks[t]:
                tp = endTime[i]
                if tp < len(dp):
                    dp[t] = max(dp[t], profit[i] + dp[tp])
                else:
                    dp[t] = max(dp[t], profit[i])
        return dp[start]

