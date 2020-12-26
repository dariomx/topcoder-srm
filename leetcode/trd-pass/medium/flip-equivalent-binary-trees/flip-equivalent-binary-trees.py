class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None and root2 is not None:
            return False
        elif root1 is not None and root2 is None:
            return False
        elif root1.val == root2.val:
            return (self.flipEquiv(root1.left, root2.left) and \
                    self.flipEquiv(root1.right, root2.right)) or \
                   (self.flipEquiv(root1.left, root2.right) and \
                    self.flipEquiv(root1.right, root2.left))
        else:
            return False
