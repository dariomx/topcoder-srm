from sys import maxsize as maxint
from random import randint

k = 2
eps = 0.001


class KDTree:
    def __init__(self, x, left, right):
        self.key = x
        self.left = left
        self.right = right


class Solution:
    def median(self, xs, i):
        n = len(xs)
        m = max(min(10, n), int(n * .01))
        R = list(range(m))
        for j in range(m, n):
            k = randint(0, j)
            if j < m:
                R[k] = j
        R.sort(key=lambda j: xs[j][i])
        return xs[R[m // 2]]

    def build_kdtree(self, xs, lev):
        if not xs:
            return None
        i = lev % k
        med = self.median(xs, i)
        left = [x for x in xs if x[i] <= med[i] and x != med]
        right = [x for x in xs if x[i] > med[i]]
        return KDTree(med,
                      self.build_kdtree(left, lev + 1),
                      self.build_kdtree(right, lev + 1))

    def rsearch(self, t, low, high, lev):
        if t is None:
            return 0
        cnt = 0
        i = lev % k
        if t.key[i] >= low[i]:
            cnt += self.rsearch(t.left, low, high, lev + 1)
        j = 0
        while j < k and low[j] <= t.key[j] <= high[j]:
            j += 1
        if j == k:
            cnt += 1
        if t.key[i] < high[i]:
            cnt += self.rsearch(t.right, low, high, lev + 1)
        return cnt

    def overlap(self, rectangles, points):
        kdtree = self.build_kdtree(points, 0)
        for x1, y1, x2, y2 in rectangles:
            low = [x1, y1]
            high = [x2 - eps, y2 - eps]
            if self.rsearch(kdtree, low, high, 0) != 4:
                return True
        return False

    def isRectangleCover(self, rectangles):
        seen = set()
        points = set()
        start = (maxint, maxint)
        end = (0, 0)
        area = 0
        for x1, y1, x2, y2 in rectangles:
            if (x1, y1, x2, y2) in seen:
                return False
            seen.add((x1, y1, x2, y2))
            area += (x2 - x1) * (y2 - y1)
            start = min(start, (x1, y1))
            end = max(end, (x2, y2))
            x2 -= eps
            y2 -= eps
            for x, y in ((x1, y1), (x2, y1), (x1, y2), (x2, y2)):
                points.add((x, y))
        x1, y1 = start
        x2, y2 = end
        return (x2 - x1) * (y2 - y1) == area and \
               not self.overlap(rectangles, list(points))

