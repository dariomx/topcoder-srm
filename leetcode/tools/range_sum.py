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
        return self.psum[end] - self.psum[start] + self.A[start]
