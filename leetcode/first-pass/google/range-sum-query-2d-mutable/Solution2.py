class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.quad_sum = dict()
        n = len(matrix)
        if n > 0:
            m = len(matrix[0])
        if n > 0 and m > 0:
            self.max_size = max(n, m)
            self.quads_x_corner = self.fillCanonQuads(matrix)
            self.empty = False
        else:
            self.empty = True

    def fillCanonQuads(self, matrix):
        n, m = len(matrix), len(matrix[0])
        quads_x_corner = [[set() for _ in xrange(m)] for _ in xrange(n)]
        self.setCanonSum(0, 0, matrix[0][0])
        quads_x_corner[0][0].add(self.hashQuad(0, 0, 0, 0))

        def addQuad(x, y):
            qhash = self.hashQuad(0, 0, x, y)
            quads_x_corner[x][y].add(qhash)
            quads_x_corner[0][0].add(qhash)

        for i in xrange(1, min(m, n)):
            lineSum = 0
            for k in xrange(i):
                lineSum += matrix[i][k]
                qsum = self.getCanonSum(i - 1, k) + lineSum
                self.setCanonSum(i, k, qsum)
                addQuad(i, k)
            lineSum = 0
            for k in xrange(i):
                lineSum += matrix[k][i]
                qsum = self.getCanonSum(k, i - 1) + lineSum
                self.setCanonSum(k, i, qsum)
                addQuad(k, i)
            qsum = self.getCanonSum(i - 1, i) + self.getCanonSum(i, i - 1) \
                   - self.getCanonSum(i - 1, i - 1) + matrix[i][i]
            self.setCanonSum(i, i, qsum)
            addQuad(i, i)
        if n > m:
            for i in xrange(m, n):
                lineSum = 0
                for k in xrange(m):
                    lineSum += matrix[i][k]
                    qsum = self.getCanonSum(i - 1, k) + lineSum
                    self.setCanonSum(i, k, qsum)
                    addQuad(i, k)
        elif n < m:
            for i in xrange(n, m):
                lineSum = 0
                for k in xrange(n):
                    lineSum += matrix[k][i]
                    qsum = self.getCanonSum(k, i - 1) + lineSum
                    self.setCanonSum(k, i, qsum)
                    addQuad(k, i)
        return quads_x_corner

    def setCanonSum(self, row2, col2, qsum):
        qhash = self.hashQuad(0, 0, row2, col2)
        self.quad_sum[qhash] = qsum

    def getCanonSum(self, row2, col2):
        qhash = self.hashQuad(0, 0, row2, col2)
        return self.quad_sum[qhash]

    def hashQuad(self, *coords):
        qhash = 0
        pow_size = 1
        for c in reversed(coords):
            qhash += c * pow_size
            pow_size *= self.max_size
        return qhash

    def update(self, row, col, val):
        if self.empty:
            return
        oldVal = self.matrix[row][col]
        for qhash in self.quads_x_corner[row][col]:
            self.quad_sum[qhash] += val - oldVal
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        if self.empty:
            return 0
        howManySubs = 0
        qsum = self.getCanonSum(row2, col2)
        if col1 - 1 >= 0:
            qsum -= self.getCanonSum(row2, col1 - 1)
            howManySubs += 1
        if row1 - 1 >= 0:
            qsum -= self.getCanonSum(row1 - 1, col2)
            howManySubs += 1
        if howManySubs == 2:
            qsum += self.getCanonSum(row1 - 1, col1 - 1)
        return qsum


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
matrix = [[1, 2]]
mat = NumMatrix(matrix)
print(mat.sumRegion(0, 0, 0, 0))
print(mat.sumRegion(0, 1, 0, 1))
print(mat.sumRegion(0, 0, 0, 1))
mat.update(0, 0, 3)
print(mat.sumRegion(0, 0, 0, 0))
print(mat.sumRegion(0, 1, 0, 1))
print(mat.sumRegion(0, 0, 0, 1))
# print(mat.sumRegion(2, 1, 4, 3))
# mat.update(3, 2, 2)
# print(mat.sumRegion(2, 1, 4, 3))
