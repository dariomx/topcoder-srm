class Solution:
    def sumOfLeftLeaves(self, root):
        def rec(node, is_left):
            if not node:
                return 0
            elif is_left and (not node.left and not node.right):
                return node.val
            else:
                return rec(node.left, True) + rec(node.right, False)

        return rec(root, False)
