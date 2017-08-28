from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        airports = set()
        for src, dst in tickets:
            graph[src].append(dst)
            airports.add(src)
            airports.add(dst)
        start = 'JFK'
        stack = [(start, [], set())]
        min_path = None
        while stack:
            node, path, visited = stack.pop()
            path.append(node)
            visited.add(node)
            if len(visited) == len(airports):
                if min_path is None:
                    min_path = path
                else:
                    min_path = min(min_path, path)
            else:
                for n in graph[node]:
                    stack.append((n, list(path), set(visited)))
        return min_path
