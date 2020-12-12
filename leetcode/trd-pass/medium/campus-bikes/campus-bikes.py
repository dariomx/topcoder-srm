# in theory using a min-heap would be faster, but it times out
from itertools import product as prod


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> \
    List[int]:
        pairs = []

        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(
                workers[w][1] - bikes[b][1])

        n, m = len(workers), len(bikes)
        for w, b in prod(range(n), range(m)):
            key = (dist(w, b), w, b)
            pairs.append((key, w, b))
        pairs.sort()
        n = len(workers)
        ans = [None] * n
        used_w, used_b = [False] * n, [False] * m
        asg_w = 0
        for _, w, b in pairs:
            if used_w[w] or used_b[b]:
                continue
            ans[w] = b
            used_w[w] = True
            used_b[b] = True
            asg_w += 1
        return ans
