from collections import defaultdict


class Solution(object):
    def build_graph(self, words):
        graph = defaultdict(list)
        for word in words:
            for c in word:
                graph[c].append(word)
                graph[word].append(c)
        return graph

    def dfs(self, start, graph, visited):
        stack = [start]
        max_len = 0
        while stack:
            word = stack.pop()
            if word in visited:
                continue
            visited.add(word)
            max_len = max(max_len, len(word))
            for w in graph[word]:
                stack.append(w)
        print(max_len)
        return max_len

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        graph = self.build_graph(words)
        visited = set()
        max1, max2 = 0, 0
        for c in graph:
            if c in visited:
                continue
            max_c = self.dfs(c, graph, visited)
            if max_c > max1:
                max2 = max1
                max1 = max_c
            elif max_c > max2:
                max2 = max_c
        return max1 * max2
