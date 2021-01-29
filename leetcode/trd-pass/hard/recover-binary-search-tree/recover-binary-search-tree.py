class Solution:
    @cache
    def min(self, node):
        if node is None:
            return None
        else:
            return min(node, self.min(node.left), self.min(node.right),
                       key=lambda n: n.val if n else inf)

    @cache
    def max(self, node):
        if node is None:
            return None
        else:
            return max(node, self.max(node.left), self.max(node.right),
                       key=lambda n: n.val if n else -inf)

    def recoverTree(self, root: TreeNode) -> None:
        if root:
            maxLeft = self.max(root.left)
            minRight = self.min(root.right)
            if maxLeft and maxLeft.val > root.val and \
                    (minRight is None or minRight.val > root.val):
                root.val, maxLeft.val = maxLeft.val, root.val
                return
            if minRight and minRight.val < root.val and \
                    (maxLeft is None or maxLeft.val < root.val):
                root.val, minRight.val = minRight.val, root.val
                return
            if maxLeft and minRight and maxLeft.val > minRight.val:
                maxLeft.val, minRight.val = minRight.val, maxLeft.val
                return
            self.recoverTree(root.left)
            self.recoverTree(root.right)
