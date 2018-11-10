class Solution:
    def hasPathSum(self, root, sum):
        def rec(node, S):
            if not node:
                return False
            elif not node.left and not node.right:
                return S == node.val
            else:
                S -= node.val
                return rec(node.left, S) or rec(node.right, S)

        return rec(root, sum)

