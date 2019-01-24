from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans = []
        level = []

        def add_level(depth):
            nonlocal level, ans
            if depth % 2 == 1:
                level.reverse()
            ans.append(level)
            level = []

        queue = deque([(root, 0)])
        prev_depth = None
        while queue:
            node, depth = queue.popleft()
            if level and depth != prev_depth:
                add_level(depth - 1)
                prev_depth = depth
            level.append(node.val)
            for child in (node.left, node.right):
                if child:
                    queue.append((child, depth + 1))
        add_level(depth)
        return ans
