from collections import defaultdict


class MinPath:
    def __init__(self):
        self.path = None

    def update(self, path):
        if self.path is None:
            self.path = path
        else:
            self.path = min(self.path, path)


class Solution(object):
    def recFindItiner(self, graph, node, path, edges, k, min_path):
        if len(edges) == k:
            min_path.update(path)
        else:
            for n in graph[node]:
                edges.add((node, n))
                self.recFindItiner(graph, n, path + [n], \
                                   edges, k, min_path)
                edges.remove((node, n))

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        min_path = MinPath()
        start = 'JFK'
        self.recFindItiner(graph, start, [start], set(), \
                           len(tickets), min_path)
        return min_path.path
