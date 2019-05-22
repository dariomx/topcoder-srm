WHITE = 1
GRAY = 2
BLACK = 3

from collections import defaultdict


class Solution:
    def build_graph(self, edges):
        graph = defaultdict(lambda: [])
        for u, v in edges:
            graph[u].append(v)
        return graph

    def dfs(self, node, graph, color, ans):
        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == GRAY:
                raise ValueError()
            elif color[nei] == WHITE:
                self.dfs(nei, graph, color, ans)
        color[node] = BLACK
        ans.append(node)

    def findOrder(self, numCourses, prerequisites):
        color = [WHITE] * numCourses
        graph = self.build_graph(prerequisites)
        ans = []
        for course in range(numCourses):
            if color[course] == WHITE:
                try:
                    self.dfs(course, graph, color, ans)
                except ValueError:
                    return []
        return ans
