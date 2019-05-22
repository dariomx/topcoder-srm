from math import inf


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costs = {1: costs[0], 7: costs[1], 30: costs[2]}
        start, end = days[0], days[-1]
        days = set(days)
        dp = [inf] * (365 + 1 + max(costs))
        for i in range(end + 1, len(dp)):
            dp[i] = 0
        for i in reversed(range(start, end + 1)):
            if i in days:
                dp[i] = min(c + dp[i + d] for (d, c) in costs.items())
            else:
                dp[i] = dp[i + 1]
        return dp[start]

