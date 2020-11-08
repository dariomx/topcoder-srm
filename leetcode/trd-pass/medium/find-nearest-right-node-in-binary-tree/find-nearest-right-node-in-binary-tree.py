class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = deque([(root, 0)])
        found = None
        prevLevel = -1
        while queue:
            node, level = queue.popleft()
            if level != prevLevel:
                found = None
                prevLevel = level
            if node == u:
                found = node
            elif found:
                return node
            for child in (node.left, node.right):
                if child:
                    queue.append((child, level + 1))
        return None
