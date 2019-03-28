# Pseudo-Canonical application of Dijkstra's Algorithm.
# Given we lack decrease-key operation, we add redundant entries in
# the min-heap; trick taken from
# https://stackoverflow.com/questions/6267172/which-datatype-to-use-as-queue
# -in-dijkstras-algorithm

# i also cheated cause saw the editorial solution, i knew that it was
# not possible to keep a single distance (cost), but was not sure if
# i should remember that per incoming node. editorial soln does it
# per stop.

# another thing i stole is that i was not exiting the function asap
# (when reached destination); this is cause i was not sure if the
# optimality was preserved and rather, i needed to exhaust all pending
# paths. but there was something fishy, the fact that i was not
# checking the "base case" (reaching dst) outside loop.

from heapq import heappop, heappush
from math import inf
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
