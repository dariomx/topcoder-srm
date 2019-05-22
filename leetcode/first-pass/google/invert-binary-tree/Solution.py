class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        else:
            inv = TreeNode(root.val)
            inv.left = self.invertTree(root.right)
            inv.right = self.invertTree(root.left)
            return inv
