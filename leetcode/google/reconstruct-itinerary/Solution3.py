from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        i = 0
        edges = dict()
        for src, dst in tickets:
            graph[src].append(dst)
            edges[(src, dst)] = i
            i += 1
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
                    new_edges = visited | set([edges[(node, n)]])
                    stack.append((n, path + [n], new_edges))
        return min_path
