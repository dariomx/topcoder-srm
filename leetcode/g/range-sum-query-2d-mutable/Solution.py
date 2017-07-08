class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.quad_sum = dict()
        n, m = len(matrix), len(matrix[0])
        self.point_x_quad = \
            [[list() for _ in xrange(m)] for _ in xrange(n)]
        self.max_size = max(n, m)

    def hashQuad(self, *coords):
        qhash = 0
        pow_size = 1
        for c in reversed(coords):
            qhash += c * pow_size
            pow_size *= self.max_size
        return qhash

    def update(self, row, col, val):
        oldVal = self.matrix[row][col]
        for qhash in self.point_x_quad[row][col]:
            self.quad_sum[qhash] += val - oldVal
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        qhash = self.hashQuad(row1, col1, row2, col2)
        if qhash not in self.quad_sum:
            qsum = 0
            for i in xrange(row1, row2+1):
                for j in xrange(col1, col2+1):
                    qsum += self.matrix[i][j]
                    self.point_x_quad[i][j].append(qhash)
            self.quad_sum[qhash] = qsum
        return self.quad_sum[qhash]

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
mat = NumMatrix(matrix)
print(mat.sumRegion(2, 1, 4, 3))
mat.update(3, 2, 2)
print(mat.sumRegion(2, 1, 4, 3))

