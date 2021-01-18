# not sure why this is not faster, mmm

class BinMatrix:
    def __init__(self, m, n, bits=0):
        self.m = m
        self.n = n
        self.bits = bits

    @staticmethod
    def convert(mat):
        m, n = len(mat), len(mat[0])
        B = BinMatrix(m, n)
        for i in range(m):
            for j in range(n):
                B.set(i, j, mat[i][j])
        return B

    def get(self, i, j):
        k = i * self.n + j
        return (self.bits & (1 << k)) >> k

    def set(self, i, j, bit):
        k = i * self.n + j
        self.bits = (self.bits & ~(1 << k)) | (bit << k)

    def flip(self, i, j):
        self.set(i, j, 1 - self.get(i, j))

    def flip_nei(self, i, j):
        self.flip(i, j)
        for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= ni < self.m and 0 <= nj < self.n:
                self.flip(ni, nj)

    def encode(self):
        return self.bits


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        state = BinMatrix.convert(mat).encode()
        if state == 0:
            return 0
        m, n = len(mat), len(mat[0])
        queue = deque([(state, 0)])
        visited = {state}
        while queue:
            state, dist = queue.popleft()
            B = BinMatrix(m, n, state)
            for i in range(m):
                for j in range(n):
                    B.flip_nei(i, j)
                    new_state = B.encode()
                    if new_state == 0:
                        return dist + 1
                    elif new_state not in visited:
                        queue.append((new_state, dist + 1))
                        visited.add(new_state)
                    B.flip_nei(i, j)
        return -1
