class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0

        def rec(node):
            nonlocal ans
            if not node:
                return 0
            elif not node.left and not node.right:
                return node.val - 1
            else:
                left = rec(node.left)
                ans += abs(left)
                right = rec(node.right)
                ans += abs(right)
                return node.val + left + right - 1

        rec(root)
        return ans
