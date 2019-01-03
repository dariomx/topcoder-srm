class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        total = m * n
        x, y = 0, 0
        ans = []
        def add(i, j):
            ans.append(matrix[x+i][y+j])
        while len(ans) < total:
            for j in range(n):
                add(0, j)
            for i in range(1, m-1):
                add(i, n-1)
            if m > 1:
                for j in range(n-1, -1, -1):
                    add(m-1, j)
            if n > 1:
                for i in range(m-2, 0, -1):
                    add(i, 0)
            x += 1
            y += 1
            m -= 2
            n -= 2
        return ans