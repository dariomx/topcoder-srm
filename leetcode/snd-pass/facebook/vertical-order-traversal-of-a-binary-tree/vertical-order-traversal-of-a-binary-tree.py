# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        reports = defaultdict(lambda: [])
        stack = [(root, 0, 0, 0)]
        while stack:
            node, d, x, y = stack.pop()
            reports[x].append((d, node.val))
            if node.left:
                stack.append((node.left, d+1, x-1, y-1))
            if node.right:
                stack.append((node.right, d+1, x+1, y-1))
        reports = sorted(reports.items(), key=lambda t: t[0])
        sort_vs = lambda vs: [x for (_, x) in sorted(vs)]
        return [sort_vs(vs) for (_, vs) in reports]