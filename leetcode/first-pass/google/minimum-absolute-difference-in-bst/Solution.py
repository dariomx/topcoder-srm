from sys import maxsize as maxint

class Solution:
    def getMinimumDifference(self, root):
        def inorder(node):
            if node:
                if node.left:
                    yield from inorder(node.left)
                yield node.val
                if node.right:
                    yield from inorder(node.right)
        inorder_gen = inorder(root)
        prev = next(inorder_gen)
        mindiff = maxint
        for val in inorder_gen:
            mindiff = min(mindiff, abs(val - prev))
            prev = val
        return mindiff