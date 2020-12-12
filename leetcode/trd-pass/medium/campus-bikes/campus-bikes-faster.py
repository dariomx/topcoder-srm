# looks like trick was to use count-sort to achieve linear time for #pairs
from itertools import product as prod


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> \
    List[int]:
        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(
                workers[w][1] - bikes[b][1])

        n, m = len(workers), len(bikes)
        pairs = defaultdict(list)
        for w, b in prod(range(n), range(m)):
            d = dist(w, b)
            pairs[d].append((w, b))
        n = len(workers)
        ans = [None] * n
        used_w, used_b = [False] * n, [False] * m
        asg_w = 0
        for d in range(2000):
            for w, b in pairs[d]:
                if used_w[w] or used_b[b]:
                    continue
                ans[w] = b
                used_w[w] = True
                used_b[b] = True
                asg_w += 1
            if asg_w == n:
                break
        return ans
