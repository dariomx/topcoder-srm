class Solution(object):
    def get_pacific_nodes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        nodes = []
        for i in xrange(m):
            nodes.append((i, 0))
        for j in xrange(1, n):
            nodes.append((0, j))
        return nodes

    def get_atlantic_nodes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        nodes = []
        for i in xrange(m):
            nodes.append((i, n - 1))
        for j in xrange(n - 1):
            nodes.append((m - 1, j))
        return nodes

    def get_children(self, matrix, x, y):
        m, n = len(matrix), len(matrix[0])
        for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i < m and 0 <= j < n and \
                            matrix[i][j] >= matrix[x][y]:
                yield (i, j)

    def search_peaks_dfs(self, matrix, stack, reached_ocean):
        peaks = set()
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            higher = 0
            x, y = node
            for c in self.get_children(matrix, x, y):
                i, j = c
                if matrix[i][j] > matrix[x][y]:
                    higher += 1
                stack.append(c)
            if higher == 0 or reached_ocean(node):
                peaks.add(node)
        return peaks

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        reached_pacific = lambda (i, j): 0 in (i, j)
        reached_atlantic = lambda (i, j): i == (m - 1) or j == (n - 1)
        pacific_nodes = self.get_pacific_nodes(matrix)
        pacific_peaks = set(pacific_nodes)
        pacific_peaks |= self.search_peaks_dfs(matrix, pacific_nodes, reached_atlantic)
        print(pacific_peaks)
        atlantic_nodes = self.get_atlantic_nodes(matrix)
        atlantic_peaks = set(atlantic_nodes)
        atlantic_peaks |= self.search_peaks_dfs(matrix, atlantic_nodes, reached_pacific)
        print(atlantic_peaks)
        return sorted(pacific_peaks & atlantic_peaks)

