from math import inf

class Solution:
    def getMinimumDifference(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        inorder_gen = inorder(root)
        prev = next(inorder_gen)
        mindiff = inf
        for val in inorder_gen:
            mindiff = min(mindiff, abs(val - prev))
            prev = val
        return mindiff