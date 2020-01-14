from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root):
        cols = defaultdict(lambda: [])
        queue = deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            if node is not None:
                cols[col].append(node.val)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        return [cols[k] for k in sorted(cols.keys())]

