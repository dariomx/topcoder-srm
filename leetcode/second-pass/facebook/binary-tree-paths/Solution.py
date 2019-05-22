"""
Python3 solution using DFS

Not much to add: we use iterative DFS with an stack, and the state for each
node its the parent's path. Every time we find a leaf, we append its path to
the global solutions list.

Complexity is that of DFS for binary trees: O(V + E) = O(n + 2n) = O(n)
"""

class Solution:
    def binaryTreePaths(self, root):
        paths = []
        stack = []
        if root:
            stack.append((root, ""))
        visited = set()
        while stack:
            node, path = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if path:
                path += "->"
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                for child in (node.left, node.right):
                    if child:
                        stack.append((child, path))
        return paths

