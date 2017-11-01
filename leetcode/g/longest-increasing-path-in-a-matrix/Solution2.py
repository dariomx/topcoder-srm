class Solution(object):
    def neighbors(self, matrix, i, j):
        n, m = len(matrix), len(matrix[0])
        for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < n and 0 <= y < m:
                yield (x, y)

    def is_start(self, matrix, i, j):
        for (x, y) in self.neighbors(matrix, i, j):
            if matrix[x][y] < matrix[i][j]:
                return False
        return True

    def min_gt_neighbor(self, matrix, i, j):
        gt = lambda (x, y): matrix[x][y] > matrix[i][j]
        gt_neighbors = filter(gt, self.neighbors(matrix, i, j))
        val = lambda (i, j): matrix[i][j]
        if gt_neighbors:
            yield min(gt_neighbors, key=val)

    def search_dfs(self, matrix, start):
        visited = set()
        stack = [(start, 1)]
        max_len = 0
        while stack:
            node, d = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            max_len = max(max_len, d)
            i, j = node
            for (x, y) in self.min_gt_neighbor(matrix, i, j):
                stack.append(((x, y), d + 1))
        return max_len

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n, m = len(matrix), 0
        if n > 0:
            m = len(matrix[0])
        if 0 in (n, m):
            return 0
        max_len = 0
        for i in xrange(n):
            for j in xrange(m):
                if self.is_start(matrix, i, j):
                    max_len = max(max_len, self.search_dfs(matrix, (i, j)))
        return max_len

