# Pseudo-Canonical application of Dijkstra's Algorithm.
# Given we lack decrease-key operation, we add redundant entries in
# the min-heap; trick taken from
# https://stackoverflow.com/questions/6267172/which-datatype-to-use-as-queue
# -in-dijkstras-algorithm

# i stole the last touch from leonmak soln, as alternative to editorial
# soln which kept track of smallest distance (cost) per #stops. here
# it looks like we dont need Dikjstra's check for improvement, so the
# trick must be attained by using min-heap and expanding from there.
# this soln from leonmak actually keeps track of the cost per path,
# which is really what i wanted originally but did not manage to see.

from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def getGraph(self, flights):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, K: int) -> int:
        heap = [(0, src, 0)]
        graph = self.getGraph(flights)
        while heap:
            cost, u, stops = heappop(heap)
            if stops > K:
                continue
            if u == dst:
                return cost
            for v, w in graph[u]:
                nstops = stops + int(v != dst)
                heappush(heap, (cost + w, v, nstops))
        return -1
