from collections import deque

class Solution:
    def connect(self, root):
        queue = deque()
        if root:
            queue.append((root, 0))
        prev_node, prev_level = None, -1
        while queue:
            node, level = queue.popleft()
            if prev_node and prev_level == level:
                prev_node.next = node
            prev_node, prev_level = node, level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
