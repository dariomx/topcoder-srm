class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def rec(k, heap):
            nonlocal ans
            if k == 0:
                ans = min(ans, -heap[0])
            else:
                dist = -heappop(heap)
                for i in range(1, k + 1):
                    dist_i = dist / (i + 1)
                    heap_i = list(heap)
                    for _ in range(i + 1):
                        heappush(heap_i, -dist_i)
                    rec(k - i, heap_i)

        heap = [stations[i - 1] - stations[i] for i in range(1, len(stations))]
        heapify(heap)
        ans = inf
        rec(K, heap)
        return ans