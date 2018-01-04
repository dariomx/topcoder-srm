"""
Python3 solution: detecting last node per level with BFS

I had some issues understanding the statement, but one fried explained me
that this is like standing (physically) on the right side of the tree and
listing the "visible" nodes; that is, those not hidden by others.

For this we just need to detect the last node per level, assuming that we
number each level from left to right. The standard way of processing nodes
per level is BFS, and we just add a distance field to each node in order to
detect the last ones: a node is the last in level if there are no more nodes
in queue, or, if next one has a different distance from root.

The complexity is same as BFS: O(V) ... Wikipedia says is O(V + E), but E will
be bounded by 2V, so I guess that is why we just say O(V).
"""

from collections import deque

class Solution:
    def rightSideView(self, root):
        rtside = []
        queue = deque()
        if root:
            queue.append((root, 0))
        visited = set()
        while queue:
            node, d = queue.popleft()
            if not queue or d != queue[0][1]:
                rtside.append(node.val)
            for c in (node.left, node.right):
                if c and c not in visited:
                    visited.add(c)
                    queue.append((c, d+1))
        return rtside