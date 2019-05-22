"""
Python3 solution using LeetCode format and two queues

Used same (or similar) format that LeetCode.com. For serializing I am using
BFS to generate level order, left to right. Any non null node is guaranteed
to have its both children in the serialization (even if these are null).

For de-serializing we just keep a couple of queues, one for pulling the roots
and the other for the children. Initially, the serialization gets parsed and
stored into the children queue; the first item is pulled and placed into the
roots queue. Then, then main loop pulls next root, then its two children, and
the children are also appended as roots.

Time and space complexities look like O(n) [inherited from BFS]
"""

from collections import deque


class Codec:
    def node2str(self, node):
        if node is None:
            return 'N'
        else:
            return str(node.val)

    def str2node(self, s):
        if s == 'N':
            return None
        else:
            return TreeNode(int(s))

    def serialize(self, root):
        visited = set()
        bfs_order = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            bfs_order.append(self.node2str(node))
            if node:
                for c in ((node.left, node.right)):
                    if c is None or c not in visited:
                        visited.add(c)
                        queue.append(c)
        return ','.join(bfs_order)

    def deserialize(self, data):
        children = deque(map(self.str2node, data.split(',')))
        root = children.popleft()
        roots = deque([root])
        while roots:
            node = roots.popleft()
            if node:
                if children:
                    node.left = children.popleft()
                    roots.append(node.left)
                if children:
                    node.right = children.popleft()
                    roots.append(node.right)
        return root
