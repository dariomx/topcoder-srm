"""
Python3 solution using BFS + binary-paths

Similarly to other problems which need to compute something per level,
we use BFS (iterative version), in order to detect the transition between one
level and the next one.

For each node we compute a path that represents the binary decisions taken
from the root up to that node, and since we append bits to the right,
the path can be taken as the numeration (left to right) of any node on its
given level.

Then, we just need to care about computing the first and the last paths per
level. That will give us the range of elements in between ... which is what
they call here the width.

Time complexity is that of BFS for binary trees: O(n)

"""

from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        queue = deque([(root, 0, 0)])
        max_width = 0
        first = None
        while queue:
            node, level, path = queue.popleft()
            if first is None:
                first = path
            if not queue or level != queue[0][1]:
                max_width  = max(max_width, path - first + 1)
                first = None
            if node.left:
                queue.append((node.left, level+1, path << 1))
            if node.right:
                queue.append((node.right, level+1, (path << 1) | 1))
        return max_width