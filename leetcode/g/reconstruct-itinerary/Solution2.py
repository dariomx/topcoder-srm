from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        edges = set()
        for src, dst in tickets:
            graph[src].append(dst)
            edges.add((src, dst))
        start = 'JFK'
        stack = [(start, [start], set())]
        min_path = None
        while stack:
            node, path, visited = stack.pop()
            if len(visited) == len(edges):
                if min_path is None:
                    min_path = path
                else:
                    min_path = min(min_path, path)
            else:
                for n in graph[node]:
                    new_edges = visited | set([(node, n)])
                    stack.append((n, path + [n], new_edges))
        return min_path
