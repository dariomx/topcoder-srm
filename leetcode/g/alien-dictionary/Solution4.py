from collections import defaultdict, deque

class Solution(object):
    def toporder_dfs(self, graph):
        def dfs(node):
            if node in visited:
                return
            elif node in stack_set:
                raise ValueError("cycle detected at %s" % str(node))
            else:
                stack_set.add(node)
                for gt_node in graph[node]:
                    dfs(gt_node)
                stack_set.remove(node)
                visited.add(node)
                queue.appendleft(node)
        queue = deque()
        visited = set()
        stack_set = set()
        for node in graph:
            dfs(node)
        return queue

    def get_chars(self, words):
        chars = set()
        for w in words:
            chars = chars.union(set(w))
        return chars

    def calc_graph(self, words):
        n = len(words)
        max_len = max(map(len, words))
        graph = defaultdict(list)
        for k in xrange(1, max_len + 1):
            for j in xrange(n - 1, 0, -1):
                w1 = words[j - 1]
                w2 = words[j]
                if len(w1) >= k and len(w2) >= k:
                    i = k-1
                    c1, c2 = w1[i], w2[i]
                    if w1[:i] == w2[:i] and c1 != c2:
                        graph[c1].append(c2)
        for c in self.get_chars(words):
            graph[c]
        return graph

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = self.calc_graph(words)
        try:
            return ''.join(self.toporder_dfs(graph))
        except ValueError, e:
            print("cycle detected: %s" % str(e))
            return ''

words = ["wrt","wrf","er","ett","rftt"]
#words = ["z", "x", "z"]
#words = ["zy", "zx"]
words = ["ac","ab","b"]
words = ["za","zb","ca","cb"]
words = ["vlxpwiqbsg","cpwqwqcd"]
print(Solution().alienOrder(words))
