from math import floor

class Solution(object):
    def imageSmoother(self, M):
        n, m = len(M), len(M[0])
        def avg(x, y):
            sum = 0
            k = 0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if 0 <= x+dx < n and 0 <= y + dy < m:
                        sum += M[x+dx][y+dy]
                        k += 1
            return floor(sum / k)
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = avg(i, j)
        return ans