from collections import defaultdict
from typing import List


class Solution:
    def _norm_edge(self, u, v):
        return tuple(sorted((u, v)))

    def _get_graph(self, connections):
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def _dfs(self, start, graph):
        stack = [(start, None)]
        visited = set()
        vedges = set()
        while stack:
            node, par = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if par is not None:
                edge = self._norm_edge(node, par)
                vedges.add(edge)
            for nei in graph[node]:
                stack.append((nei, node))
        return vedges

    def _dfs_path(self, start, end, graph):
        stack = [(start, [start])]
        visited = set()
        while stack:
            node, path = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return path
            for nei in graph[node]:
                stack.append((nei, path + [nei]))
        raise ValueError('Path not found %d -> %d' % (start, end))

    def _remove_path(self, path, edges):
        for i in range(len(path) - 1):
            edges.discard(self._norm_edge(path[i], path[i + 1]))

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[
        List[int]]:
        edges = {self._norm_edge(u, v) for u, v in connections}
        graph = self._get_graph(edges)
        span_edges = self._dfs(0, graph)
        span_graph = self._get_graph(span_edges)
        for u, v in edges - span_edges:
            path = self._dfs_path(u, v, span_graph)
            self._remove_path(path, span_edges)
        return span_edges

# main
edges = []
with open('c:/cygwin64/tmp/kk.txt') as fin:
    for line in fin:
        edge = list(map(int, line.split(',')))
        edges.append(edge)
print(Solution().criticalConnections(1000, edges))