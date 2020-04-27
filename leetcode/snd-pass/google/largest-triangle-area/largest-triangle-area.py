from typing import List

from math import inf, sqrt
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        cache = dict()

        def dist(i, j):
            if i < j:
                key = i, j
            else:
                key = j, i
            if key in cache:
                return cache[key]
            else:
                p, q = points[i], points[j]
                d = sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
                cache[key] = d
                return d

        ans = -inf
        for i, j, k in combinations(range(len(points)), 3):
            A = dist(i, j)
            B = dist(i, k)
            C = dist(j, k)
            P = (A + B + C) / 2
            area_sq = P * (P - A) * (P - B) * (P - C)
            ans = max(ans, area_sq)
        return sqrt(ans)
