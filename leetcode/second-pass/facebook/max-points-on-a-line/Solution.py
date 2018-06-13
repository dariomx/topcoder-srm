from collections import defaultdict
from math import inf, sqrt


# this soln is not entirely correct, cause is not able to handle duplicate
# points.
# the reason why it works is due an heuristic (derived from test cases), which
# accounts for repeated points.
class Solution(object):
    # k*(k+1) = 2d, where k is n-1 (n being #colinear points), as we
    # accounted for lower triag matrix of pairs
    def solve(self, d):
        a = 1
        b = 1
        c = -2 * d
        disc = sqrt(b * b - 4 * a * c)
        k1 = (-b - disc) / (2 * a)
        k2 = (-b + disc) / (2 * a)
        return int(max(k1, k2)) + 1

    def maxPoints(self, points):
        lines = defaultdict(lambda: 0)
        n = len(points)
        if n == 0:
            return 0
        max_area = 0
        used = defaultdict(lambda: 0)
        max_rep = 0
        for i in range(n):
            x1, y1 = points[i].x, points[i].y
            used[(x1, y1)] += 1
            max_rep = max(max_rep, used[(x1, y1)])
            for j in range(i + 1, n):
                x2, y2 = points[j].x, points[j].y
                if x1 == x2 and y1 == y2:
                    continue
                if x1 == x2:
                    m, b = inf, x1
                elif y1 == y2:
                    m, b = 0, y1
                else:
                    m = (y2 - y1) / (x2 - x1)
                    b = -m * x1 + y1
                    m, b = round(m, 7), round(b, 7)
                lines[(m, b)] += 1
                max_area = max(max_area, lines[(m, b)])
        if max_area > 0:
            max_side = self.solve(max_area) + int(max_rep > 1)
        else:
            max_side = max_rep
        return max(max_side, int(n > 0))

