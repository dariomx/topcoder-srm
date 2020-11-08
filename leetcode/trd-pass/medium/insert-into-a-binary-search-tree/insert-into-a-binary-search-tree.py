class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        ans = root
        if root is None:
            ans = TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return ans
