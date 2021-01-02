# for this one i saw it was tagged under dynamic programming

class Solution:
    def rob(self, root: TreeNode) -> int:
        @cache
        def rec(node, pick):
            if node is None:
                return 0
            elif pick:
                return node.val + rec(node.left, False) + rec(node.right, False)
            else:
                return max(rec(node.left, True) + rec(node.right, True),
                           rec(node.left, False) + rec(node.right, True),
                           rec(node.left, True) + rec(node.right, False),
                           rec(node.left, False) + rec(node.right, False))

        return max(rec(root, False), rec(root, True))
