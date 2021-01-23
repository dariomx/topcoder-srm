class RangeSum2D:
    def __init__(self, A, f=lambda x: x):
        n, m = len(A), len(A[0])
        psum = [[0] * m for _ in range(n+1)]
        for i in range(n):
            acc = 0
            for j in range(m):
                acc += f(A[i][j])
                psum[i][j] = psum[i-1][j] + acc
        self.psum = psum
        self.A = A
        self.f = f

    def query(self, x1, y1, x2, y2):
        ans = self.psum[x2][y2]
        if y1 > 0:
            ans -= self.psum[x2][y1-1]
        if x1 > 0:
            ans -= self.psum[x1-1][y2]
        if x1 > 0 and y1 > 0:
            ans += self.psum[x1-1][y1-1]
        return ans