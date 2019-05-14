from collections import defaultdict


class Solution:
    def buildGraph(self, root):
        graph = defaultdict(lambda: [])
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            if not node:
                continue
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            for child in (node.left, node.right):
                stack.append((child, node))
        return graph

    def distanceK(self, root, target, k):
        graph = self.buildGraph(root)
        stack = [(target.val, 0)]
        visited = set()
        ans = []
        while stack:
            node, dist = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if dist == k:
                ans.append(node)
            for child in graph[node]:
                stack.append((child, dist + 1))
        return ans
