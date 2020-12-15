"""
We can evaluate each point but without recomputing its total distance
against the other; rather we leverage the previously computed distance
and just update in O(1)
"""

class RangeSum:
    def __init__(self, A):
        n = len(A)
        psum = [0] * n
        psum[0] = A[0]
        for i in range(1, n):
            psum[i] = psum[i - 1] + A[i]
        self.psum = psum
        self.A = A

    def get(self, start, end):
        n = len(self.A)
        if 0 <= start <= end < n:
            return self.psum[end] - self.psum[start] + self.A[start]
        else:
            return 0


class Solution:
    def calcFreq(self, grid: List[List[int]]) -> Tuple[List[int], List[int]]:
        n, m = len(grid), len(grid[0])
        fv, fh = [0] * n, [0] * m
        l1norm = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fv[i] += 1
                    fh[j] += 1
                    l1norm += i + j
        return fv, fh, l1norm

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        fv, fh, l1norm = self.calcFreq(grid)
        rv, rh = RangeSum(fv), RangeSum(fh)
        n, m = len(grid), len(grid[0])
        ans, row = inf, l1norm
        for i in range(n):
            col = row
            ans = min(ans, col)
            for j in range(1, m):
                col += rh.get(0, j - 1) - rh.get(j, m - 1)
                ans = min(ans, col)
            row = row + rv.get(0, i) - rv.get(i + 1, n - 1)
        return ans
