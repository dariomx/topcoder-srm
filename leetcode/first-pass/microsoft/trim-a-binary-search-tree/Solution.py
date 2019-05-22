class Solution:
    def trimBST(self, root, L, R):
        if root is None:
            return None
        else:
            left = self.trimBST(root.left, L, R)
            right = self.trimBST(root.right, L, R)
            if L <= root.val <= R:
                root.left = left
                root.right = right
                return root
            elif left:
                return left
            else:
                return right