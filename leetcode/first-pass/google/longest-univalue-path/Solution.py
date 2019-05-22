class Solution:
    def longestUnivaluePath(self, root):
        def rec(node, pval):
            if node is None or node.val != pval:
                return 0
            else:
                left = rec(node.left, pval)
                right = rec(node.right, pval)
                return 1 + max(left, right)

        if root is None:
            return 0
        leftC = leftP = rightC = rightP = 0
        if root.left:
            leftC = self.longestUnivaluePath(root.left)
            leftP = rec(root.left, root.val)
        if root.right:
            rightC = self.longestUnivaluePath(root.right)
            rightP = rec(root.right, root.val)
        return max(leftP + rightP, leftC, rightC)
