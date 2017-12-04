# this one uses a hint from other solution, trees can
# only have n-1 edges! (that is super optimization)

from collections import defaultdict


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        graph = defaultdict(lambda: [])
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        if not graph:
            return n <= 1
        start = graph.iterkeys().next()
        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for child in graph[node]:
                stack.append(child)
        return len(visited) == n
