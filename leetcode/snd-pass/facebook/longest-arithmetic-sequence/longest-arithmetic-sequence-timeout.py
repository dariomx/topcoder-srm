"""
topoSort taken from:
https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search

longestPath from:
https://stackoverflow.com/questions/2525316/longest-acyclic-path-in-a
-directed-unweighted-graph
"""

from collections import defaultdict, deque

WHITE = 0
GRAY = 1
BLACK = 2


class Solution:
    def calcDiffGraphs(self, A):
        n = len(A)
        diffGraph = defaultdict(lambda: defaultdict(list))
        diffVertex = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                diffGraph[diff][i].append(j)
                diffVertex[diff] |= {i, j}
        return diffGraph, diffVertex

    def topoSort(self, graph, vertex):
        color = {node: WHITE for node in vertex}
        order = deque()

        def visit(node):
            if color[node] == BLACK:
                return
            elif color[node] == GRAY:
                raise ValueError("not a dag")
            color[node] = GRAY
            if node in graph:
                for nei in graph[node]:
                    visit(nei)
            color[node] = BLACK
            order.appendleft(node)

        for node in vertex:
            if color[node] == WHITE:
                visit(node)
        return order

    def longestPath(self, graph, vertex):
        dist = {node: 0 for node in vertex}
        for node in self.topoSort(graph, vertex):
            if node not in graph:
                continue
            for nei in graph[node]:
                if dist[nei] <= dist[node] + 1:
                    dist[nei] = dist[node] + 1
        return max(dist.values()) + 1

    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        diffGraphs, diffVertex = self.calcDiffGraphs(A)
        for diff, graph in diffGraphs.items():
            vertex = diffVertex[diff]
            ans = max(ans, self.longestPath(graph, vertex))
        return ans
