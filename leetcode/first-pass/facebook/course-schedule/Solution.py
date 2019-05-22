from collections import defaultdict

WHITE = 0
GRAY = 1
BLACK = 2


class Solution:
    def buildGraph(self, reqs):
        graph = defaultdict(lambda: [])
        for x, y in reqs:
            graph[y].append(x)
        return graph

    def canFinish(self, numCourses: 'int',
                  prerequisites: 'List[List[int]]') -> 'bool':
        color = [WHITE] * numCourses
        graph = self.buildGraph(prerequisites)

        def dfs(node):
            if color[node] == BLACK:
                return
            elif color[node] == GRAY:
                raise ValueError("cycle!")
            else:
                color[node] = GRAY
                for child in graph[node]:
                    dfs(child)
                color[node] = BLACK

        # main
        for node in range(numCourses):
            try:
                dfs(node)
            except:
                return False
        return True
