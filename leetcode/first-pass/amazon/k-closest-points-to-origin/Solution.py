from heapq import heappop, heapify
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda p: sqrt(p[0]*p[0] + p[1]*p[1])
        heap = [(dist(p), p) for p in points]
        heapify(heap)
        ans = []
        for _ in range(K):
            ans.append(heappop(heap)[1])
        return ans