# i was just missing a proper cache (play days were not part of key)

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        N, K = len(flights), len(days[0])
        @cache
        def rec(week, city):
            if week == K:
                return 0
            else:
                ret = -inf
                for i in range(N):
                    if i == city or flights[city][i] == 1:
                        ret = max(ret, rec(week + 1, i) + days[i][week])
                return ret
        return rec(0, 0)
