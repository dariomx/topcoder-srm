from collections import defaultdict

WHITE = 0
BLACK = 1


class Solution:
    def dfs(self, node, graph, color, parent=None):
        color[node] = BLACK
        for nei in graph[node]:
            if color[nei] == BLACK and nei != parent:
                raise ValueError("Cycle detected")
            elif color[nei] == WHITE:
                self.dfs(nei, graph, color, node)

    def validTree(self, n, edges):
        graph = defaultdict(lambda: [])
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        color = [WHITE] * n
        try:
            self.dfs(0, graph, color)
        except ValueError:
            return False
        for c in color:
            if c != BLACK:
                return False
        return True



