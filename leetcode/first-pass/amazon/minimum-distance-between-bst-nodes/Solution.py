from math import inf

class Solution:
    def minDiffInBST(self, root):
        prev = None
        ans = inf
        def inorder(node):
            nonlocal prev, ans
            if node:
                inorder(node.left)
                if prev:
                    ans = min(ans, abs(prev.val - node.val))
                prev = node
                inorder(node.right)
        inorder(root)
        return ans