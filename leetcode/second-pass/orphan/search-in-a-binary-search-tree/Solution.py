class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        elif val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)