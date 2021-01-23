MOD = 10 ** 9 + 7


class RangeSum2D:
    def __init__(self, A, f=lambda x: x):
        n, m = len(A), len(A[0])
        psum = [[0] * m for _ in range(n + 1)]
        for i in range(n):
            acc = 0
            for j in range(m):
                acc += f(A[i][j])
                psum[i][j] = psum[i - 1][j] + acc
        self.psum = psum
        self.A = A
        self.f = f

    def query(self, x1, y1, x2, y2):
        ans = self.psum[x2][y2]
        if y1 > 0:
            ans -= self.psum[x2][y1 - 1]
        if x1 > 0:
            ans -= self.psum[x1 - 1][y2]
        if x1 > 0 and y1 > 0:
            ans += self.psum[x1 - 1][y1 - 1]
        return ans


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @cache
        def count(x1, y1, x2, y2, cuts):
            if x1 > x2 or y1 > y2:
                return int(cuts == 0)
            elif cuts == 0:
                return int(rsum.query(x1, y1, x2, y2) > 0)
            else:
                cnt = 0
                for x in range(x1, x2):
                    cnt += count(x1, y1, x, y2, 0) * count(x + 1, y1, x2, y2,
                                                           cuts - 1)
                for y in range(y1, y2):
                    cnt += count(x1, y1, x2, y, 0) * count(x1, y + 1, x2, y2,
                                                           cuts - 1)
                return cnt % MOD

        m, n = len(pizza), len(pizza[0])
        rsum = RangeSum2D(pizza, lambda x: int(x == 'A'))
        return count(0, 0, m - 1, n - 1, k - 1)
