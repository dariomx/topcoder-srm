"""
Python3 solution with linear time and space

BFS provides just the order we want, and in order to detect the level
transitions we just store the current level of each node.
"""

from collections import deque

class Solution:
    def levelOrder(self, root):
        ans = []
        queue = deque()
        if root:
            queue.append((root, 0))
        prev_level = -1
        visited = set()
        while queue:
            node, level = queue.popleft()
            if level != prev_level:
                ans.append([])
                prev_level = level
            ans[-1].append(node.val)
            for child in (node.left, node.right):
                if child and child not in visited:
                    visited.add(child)
                    queue.append((child, level+1))
        return ans