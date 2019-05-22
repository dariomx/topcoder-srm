class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        else:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), \
                             self.minDepth(root.right))
            elif root.left:
                return 1 + self.minDepth(root.left)
            else:
                return 1 + self.minDepth(root.right)
