"""
Recursive Python3 solution with a tweak (range checking)

The recursive BST definition can derive directly the function,
except maybe for the additional constraint that each branch
needs to have its values within certain range of values. Every
time you go through a root node and recurse on branches, the
root's value becomes either the new min or max allowed value; depending
on whether you fork on left or right (respectively).
"""

from sys import maxsize as maxint


class Solution:
    def isValidBST(self, root):
        def isValid(root, minVal, maxVal):
            if not root:
                return True
            if not (minVal < root.val < maxVal):
                return False
            if not isValid(root.left, minVal, root.val):
                return False
            if not isValid(root.right, root.val, maxVal):
                return False
            return True

        return isValid(root, -maxint - 1, maxint)
