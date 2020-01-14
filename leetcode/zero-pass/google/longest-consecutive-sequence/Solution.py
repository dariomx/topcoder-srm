from collections import defaultdict
from sys import maxint


class Solution(object):
    def dfs(self, start, graph, visited):
        min_n, max_n = maxint, -maxint
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            min_n = min(min_n, node)
            max_n = max(max_n, node)
            for n in graph[node]:
                stack.append(n)
        return max_n - min_n + 1

    def build_graph(self, nums):
        graph = defaultdict(list)
        for n in nums:
            if n in graph:
                continue
            for m in (n - 1, n + 1):
                if m in graph:
                    graph[m].append(n)
                    graph[n].append(m)
            graph[n]
        return graph

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        graph = self.build_graph(nums)
        max_len = 0
        visited = set()
        for n in nums:
            if n not in visited:
                max_len = max(max_len, self.dfs(n, graph, visited))
        return max_len
