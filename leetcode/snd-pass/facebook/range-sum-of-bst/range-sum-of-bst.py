class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        def rec(node):
            nonlocal ans
            if node:
                if L <= node.val <= R:
                    ans += node.val
                rec(node.left)
                rec(node.right)
        rec(root)
        return ans