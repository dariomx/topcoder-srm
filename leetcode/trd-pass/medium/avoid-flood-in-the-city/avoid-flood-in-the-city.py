from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        last_rain = {}
        full = set()
        dry = SortedList()
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.add(i)
            else:
                if lake in full:
                    cand = dry.irange(minimum=last_rain[lake], inclusive=(False,True))
                    j = next(cand, None)
                    if j is None:
                        return []
                    ans[j] = lake
                    dry.remove(j)
                else:
                    full.add(lake)
                ans[i] = -1
                last_rain[lake] = i
        return ans