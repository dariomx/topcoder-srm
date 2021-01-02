class CannoRect:
    def __init__(self, A):
        n, m = len(A), len(A[0])
        csum = [[0] * m for _ in range(n)]
        csum[0][0] = A[0][0]
        for y in range(1, m):
            csum[0][y] = csum[0][y - 1] + A[0][y]
        for x in range(1, n):
            acc = 0
            for y in range(m):
                acc += A[x][y]
                csum[x][y] = acc + csum[x - 1][y]
        self.csum = csum

    def sum(self, x1, y1, x2, y2):
        ret = self.csum[x2][y2]
        if y1 - 1 >= 0:
            ret -= self.csum[x2][y1 - 1]
        if x1 - 1 >= 0:
            ret -= self.csum[x1 - 1][y2]
        if x1 - 1 >= 0 and y1 - 1 >= 0:
            ret += self.csum[x1 - 1][y1 - 1]
        return ret


class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        n, m = len(A), len(A[0])
        cRect = CannoRect(A)
        ans = 0
        for x1 in range(n):
            for y1 in range(m):
                for x2 in range(x1, n):
                    for y2 in range(y1, m):
                        if cRect.sum(x1, y1, x2, y2) == target:
                            ans += 1
        return ans
