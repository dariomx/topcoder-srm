from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        start = 'JFK'
        stack = [(start, [start], 0)]
        min_path = None
        edges = set()
        while stack:
            node, path, num_edges = stack.pop()
            if num_edges == len(tickets):
                if min_path is None:
                    min_path = path
                else:
                    min_path = min(min_path, path)
            else:
                for n in graph[node]:
                    edges.add((node, n))
                    stack.append((n, path + [n], len(edges)))
        return min_path
