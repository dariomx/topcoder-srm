class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        maxDepth = 0
        ans = 0
        def rec(node, depth):
            nonlocal maxDepth, ans
            if depth > maxDepth:
                maxDepth = depth
                ans = node.val
            elif depth == maxDepth:
                ans += node.val
            if node.left:
                rec(node.left, depth+1)
            if node.right:
                rec(node.right, depth+1)
        rec(root, 0)
        return ans