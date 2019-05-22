from math import inf


class Solution:
    def minAreaRect(self, points: 'List[List[int]]') -> 'int':
        ans = inf
        rset = set(map(tuple, points))
        for i in range(len(points)):
            for j in range(i):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in rset and (x2, y1) in rset:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    ans = min(ans, area)
        return ans if ans < inf else 0
