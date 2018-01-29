"""
Python3 solution with O(n) time and space

I could not figure out a solution that only used recursion, hence came up
with an in-order traversal; and once I have elements aligned then I just
compute the prefix sums from right to left.
"""

class Solution:
    def convertBST(self, root):
        inorder = []
        def traverse(root):
            if root is None:
                return
            else:
                traverse(root.left)
                inorder.append(root)
                traverse(root.right)
        traverse(root)
        n = len(inorder)
        for i in range(n-2, -1, -1):
            inorder[i].val += inorder[i+1].val
        return root