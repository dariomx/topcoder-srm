# RMQ is not mine, taken from
# https://gist.github.com/m00nlight/1f226777a49cfc40ed8f

from math import inf

class RMQ:
    def __init__(self, n):
        self.sz = 1
        while self.sz <= n:
            self.sz = self.sz << 1
        self.dat = [[None, -inf] for i in range(2 * self.sz - 1)]

    def __setitem__(self, idx, x):
        old_idx = idx
        idx += self.sz - 1
        self.dat[idx] = [old_idx, x]
        while idx > 0:
            idx = (idx - 1) >> 1
            self.dat[idx] = max(self.dat[idx * 2 + 1],
                                self.dat[idx * 2 + 2],
                                key=lambda x: x[1])

    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz)

    def query_help(self, a, b, k, l, r):
        if r <= a or b <= l:
            return (0, -inf)
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            return max(self.query_help(a, b, 2 * k + 1, l, (l + r)>>1),
                       self.query_help(a, b, 2 * k + 2, (l + r) >> 1, r),
                       key=lambda x: x[1])

class Solution:
    def bisect_right(self, arr, x, start, end, key):
        while start <= end:
            mid = (start + end) // 2
            if key(arr[mid]) <= x:
                start = mid + 1
            else:
                end = mid - 1
        return start


    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        rmq = RMQ(n)
        ans = -inf
        for i in reversed(range(n)):
            x1, y1 = points[i]
            end = self.bisect_right(points, x1 + k, i+1, n-1, key=lambda x: x[0])
            j, y2 = rmq.query(i, end)
            print(x1, y1, i, n-1, end, y2, j)
            if j is not None:
                x2 = points[j][0]
                ans = max(ans, y1 + y2 + abs(x1 - x2))
            rmq[i] = y1
        return ans
