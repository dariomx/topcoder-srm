from decimal import Decimal


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        line = defaultdict(set)
        cnt = defaultdict(lambda: 0)
        for i in range(n):
            x1, y1 = points[i]
            cnt[x1, y1] += 1
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                if dx == 0:
                    m = inf
                else:
                    m = Decimal(y2 - y1) / Decimal(dx)
                p = min((x1, y1), (x2, y2))
                q = max((x1, y1), (x2, y2))
                line[m, p].add(p)
                line[m, p].add(q)
        ans = 0
        for _, ps in line.items():
            ans = max(ans, sum(cnt[p] for p in ps))
        return ans


