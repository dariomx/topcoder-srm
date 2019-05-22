from math import sqrt, inf


class Solution(object):
    def constructRectangle(self, area):
        diff = inf
        l, w = 1, area
        for d in range(1, int(sqrt(area)) + 1):
            q, r = divmod(area, d)
            if r == 0 and abs(d - q) < diff:
                l, w = max(d, q), min(d, q)
        return l, w


