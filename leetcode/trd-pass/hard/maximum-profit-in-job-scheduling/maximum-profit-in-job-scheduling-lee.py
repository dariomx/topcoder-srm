# fixed my sorted-list version with clever idea from lee about
# binary-searching in dp instead
# of tasks.

from sortedcontainers import SortedList, SortedDict


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        tasks = SortedList(zip(startTime, endTime, profit), key=lambda t: t[0])
        n = len(tasks)
        dp = SortedDict()
        for i in reversed(range(n)):
            s1, e, p = tasks[i]
            if s1 in dp:
                dp[s1] = max(dp[s1], p)
            else:
                dp[s1] = p
            j = dp.bisect_left(e)
            if j < len(dp):
                s2 = dp.keys()[j]
                dp[s1] = max(dp[s1], p + dp[s2])
            k = dp.index(s1)
            if k < len(dp) - 1:
                s2 = dp.keys()[k + 1]
                dp[s1] = max(dp[s1], dp[s2])
        return max(dp.values())

