from collections import deque


class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left and right and left.val == right.val:
            return self.isMirror(left.left, right.right) and \
                   self.isMirror(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        if root:
            return self.isMirror(root.left, root.right)
        else:
            return True
