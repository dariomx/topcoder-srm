class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        elif not root.left and not root.right:
            return True
        else:
            return (root.left is None or root.val == root.left.val) and \
                   (root.right is None or root.val == root.right.val) and \
                   self.isUnivalTree(root.left) and \
                   self.isUnivalTree(root.right)
