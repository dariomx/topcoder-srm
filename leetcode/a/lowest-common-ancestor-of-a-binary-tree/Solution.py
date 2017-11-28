"""
We compute the path from root to each node using DFS, and then search
from the beginning of both paths (root) what is the last common node
they share before diverging.
"""

from itertools import izip


class Solution(object):
    def get_parent(self, root, u, v):
        stack = [root]
        visited = set()
        parent = dict()
        parent[root] = root
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            if u in visited and v in visited:
                break
        return parent

    def get_path(self, parent, end):
        node = end
        path = []
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(node)
        return reversed(path)

    def lowestCommonAncestor(self, root, p, q):
        parent = self.get_parent(root)
        path_p = self.get_path(parent, p)
        path_q = self.get_path(parent, q)
        ancestor = None
        for node_p, node_q in izip(path_p, path_q):
            if node_p != node_q:
                break
            else:
                ancestor = node_p
        return ancestor