# a tree is connected and without cycles
#
# uses iterative dfs to traverse graph and detect cycles
#
# find cycles by looking at current stack, and checking
# if current node (just popped out of stack), has another
# occurrence in stack.
#
# brute force approach when searching in stack

from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(lambda: [])
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        if not graph:
            return n <= 1
        start = graph.iterkeys().next()
        stack = [start]
        visited = set()
        while stack:
            #print(stack[-1])
            #print(visited)
            #print(stack)
            node = stack.pop()
            if node in stack:
                return False
            if node in visited:
                continue
            visited.add(node)
            for child in graph[node]:
                stack.append(child)
        return len(visited) == n