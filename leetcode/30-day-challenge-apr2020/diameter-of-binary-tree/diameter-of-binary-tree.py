from math import inf


class Solution:
    def diamDepth(self, root):
        if root is None:
            return -inf, -inf
        elif root.left is None and root.right is None:
            return 0, 0
        else:
            diamL, depthL = self.diamDepth(root.left)
            diamR, depthR = self.diamDepth(root.right)
            diam = max(depthL + 1, 0) + max(depthR + 1, 0)
            return max(diamL, diamR, diam), 1 + max(depthL, depthR)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return max(self.diamDepth(root)[0], 0)
