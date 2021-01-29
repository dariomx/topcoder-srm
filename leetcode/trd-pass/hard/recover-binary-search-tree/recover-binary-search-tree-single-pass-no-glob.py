class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def rec(node):
            if node is None:
                return None, None
            else:
                minLeft, maxLeft = rec(node.left)
                minRight, maxRight = rec(node.right)
                if maxLeft and maxLeft.val > node.val and \
                        (minRight is None or minRight.val > node.val):
                    self.change = (node, maxLeft)
                if minRight and minRight.val < node.val and \
                        (maxLeft is None or maxLeft.val < node.val):
                    self.change = (node, minRight)
                if maxLeft and minRight and maxLeft.val > minRight.val:
                    self.change = (maxLeft, minRight)
                minNode = min(minLeft, node, minRight,
                              key=lambda n: n.val if n else inf)
                maxNode = max(maxLeft, node, maxRight,
                              key=lambda n: n.val if n else -inf)
                return minNode, maxNode

        # main
        rec(root)
        x, y = self.change
        x.val, y.val = y.val, x.val
