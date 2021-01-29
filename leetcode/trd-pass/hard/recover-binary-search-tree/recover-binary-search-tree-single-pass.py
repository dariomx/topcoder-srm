class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def rec(node):
            if node is None:
                return
            else:
                self.max, self.min = None, None
                rec(node.left)
                maxLeft, minLeft = self.max, self.min
                self.max, self.min = None, None
                rec(node.right)
                maxRight, minRight = self.max, self.min
                if maxLeft and maxLeft.val > node.val and \
                        (minRight is None or minRight.val > node.val):
                    self.change = (node, maxLeft)
                if minRight and minRight.val < node.val and \
                        (maxLeft is None or maxLeft.val < node.val):
                    self.change = (node, minRight)
                if maxLeft and minRight and maxLeft.val > minRight.val:
                    self.change = (maxLeft, minRight)
                self.max = max(maxLeft, node, maxRight,
                               key=lambda n: n.val if n else -inf)
                self.min = min(minLeft, node, minRight,
                               key=lambda n: n.val if n else inf)

        # main
        rec(root)
        x, y = self.change
        x.val, y.val = y.val, x.val
