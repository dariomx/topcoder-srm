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

    def get_children(self, matrix, node):
        m, n = len(matrix), len(matrix[0])
        x, y = node
        for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i < m and 0 <= j < n and \
                            matrix[i][j] >= matrix[x][y]:
                yield (i, j)

    def search_peaks_dfs(self, matrix, stack):
        peaks = set()
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for c in self.get_children(matrix, node):
                stack.append(c)
        return visited

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        pacific_nodes = self.get_pacific_nodes(matrix)
        pacific_reach = set(pacific_nodes)
        pacific_reach |= self.search_peaks_dfs(matrix, pacific_nodes)
        # print(pacific_reach)
        atlantic_nodes = self.get_atlantic_nodes(matrix)
        atlantic_reach = set(atlantic_nodes)
        atlantic_reach |= self.search_peaks_dfs(matrix, atlantic_nodes)
        # print(atlantic_reach)
        return list(pacific_reach & atlantic_reach)
