# same as Solution, but with a faster search in stack
# (use a counter to keep track of current occurrences
# of each node in stack).

from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        graph = defaultdict(lambda: [])
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        if not graph:
            return n <= 1
        start = graph.iterkeys().next()
        stack = [start]
        visited = set()
        cnt = defaultdict(lambda: 0)
        cnt[start] = 1
        while stack:
            node = stack.pop()
            cnt[node] -= 1
            if cnt[node] > 0:
                return False
            if node in visited:
                continue
            visited.add(node)
            for child in graph[node]:
                stack.append(child)
                cnt[child] += 1
        return len(visited) == n