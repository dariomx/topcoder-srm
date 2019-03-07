from collections import deque

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        used = set()
        ans = []
        while queue:
            node = queue.popleft()
            if node in used:
                ans.append(node.val)
            else:
                if node.right:
                    queue.appendleft(node.right)
                queue.appendleft(node)
                if node.left:
                    queue.appendleft(node.left)
                used.add(node)
        return ans