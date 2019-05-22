class Solution:
    def isBalanced(self, root):
        def maxDepth(node):
            if node is None:
                return 0
            else:
                left = 1 + maxDepth(node.left)
                right = 1 + maxDepth(node.right)
                if abs(left - right) > 1:
                    raise ValueError()
                else:
                    return max(left, right)

        try:
            maxDepth(root)
            return True
        except:
            return False
