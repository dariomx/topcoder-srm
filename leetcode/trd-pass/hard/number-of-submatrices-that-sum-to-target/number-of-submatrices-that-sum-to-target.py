class VertBand:
    def __init__(self, A):
        n, m = len(A), len(A[0])
        vsum = [[0] * n for _ in range(m)]
        for j in range(m):
            vsum[j][0] = A[0][j]
        for j in range(m):
            for i in range(1, n):
                vsum[j][i] += vsum[j][i - 1] + A[i][j]
        self.vsum = vsum
        self.A = A

    def band(self, x1, x2):
        m = len(self.A[0])
        for j in range(m):
            yield self.vsum[j][x2] - self.vsum[j][x1] + self.A[x1][j]


class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        n, m = len(A), len(A[0])
        vBand = VertBand(A)
        ans = 0
        for x1 in range(n):
            for x2 in range(x1, n):
                psum = 0
                seen = defaultdict(lambda: 0)
                for y in vBand.band(x1, x2):
                    psum += y
                    if psum == target:
                        ans += 1
                    need = psum - target
                    if need in seen:
                        ans += seen[need]
                    seen[psum] += 1
        return ans
