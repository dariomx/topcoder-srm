from sortedcontainers import SortedList


class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def rec(k, sl):
            nonlocal ans
            if k == 0:
                ans = min(ans, sl[-1])
            else:
                dist = sl[-1]
                sl.remove(dist)
                for i in range(1, k + 1):
                    dist_i = dist / (i + 1)
                    for _ in range(i + 1):
                        sl.add(dist_i)
                    rec(k - i, sl)
                    for _ in range(i + 1):
                        sl.discard(dist_i)
                sl.add(dist)

        sl = SortedList(
            [stations[i] - stations[i - 1] for i in range(1, len(stations))])
        ans = inf
        rec(K, sl)
        return ans