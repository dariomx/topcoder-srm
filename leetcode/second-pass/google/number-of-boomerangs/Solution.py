from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points):
        n = len(points)
        dist = defaultdict(lambda: 0)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dist[(i, d)] += 1
                dist[(j, d)] += 1
        ans = 0
        for _, n in dist.items():
            if n > 1:
                ans += n * (n - 1)
        return ans
