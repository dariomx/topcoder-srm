from heapq import heappop, heapify
from math import inf


class Solution:
    def networkDelayTime(self, times, N, K):
        graph = [[] for _ in range(N + 1)]
        entry = {K: [0, K]}
        heap = [entry[K]]
        for u, v, w in times:
            graph[u].append((v, w))
            if u not in entry:
                entry[u] = [inf, u]
                heap.append(entry[u])
            if v not in entry:
                entry[v] = [inf, v]
                heap.append(entry[v])
        heapify(heap)
        dist = [inf] * (N + 1)
        dist[0] = 0
        dist[K] = 0
        while heap:
            _, node = heappop(heap)
            for nei, w in graph[node]:
                alt = dist[node] + w
                if alt < dist[nei]:
                    dist[nei] = alt
                    entry[nei][0] = alt
                    heapify(heap)
        ans = max(dist)
        return -1 if ans == inf else ans


