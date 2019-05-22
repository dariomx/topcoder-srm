from collections import defaultdict

WHITE = 0
GRAY = 1
BLACK = 2


class Solution:
    def findOrder(self, numCourses, prerequisites):
        order = []
        color = dict(((n, WHITE) for n in range(numCourses)))
        graph = defaultdict(lambda: [])
        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(node):
            if color[node] == BLACK:
                return True
            elif color[node] == GRAY:
                return False
            else:
                color[node] = GRAY
                for nei in graph[node]:
                    if not dfs(nei):
                        return False
                color[node] = BLACK
                order.append(node)
                return True

        for node in range(numCourses):
            if color[node] == WHITE:
                if not dfs(node):
                    return []
        return order if len(order) == numCourses else []

