from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        ans = []
        prev = -1
        if root:
            queue.append((root, 0))
        while queue:
            node, lev = queue.popleft()
            if lev != prev:
                prev = lev
                ans.append([])
            ans[-1].append(node.val)
            for child in (node.left, node.right):
                if child:
                    queue.append((child, lev + 1))
        return ans