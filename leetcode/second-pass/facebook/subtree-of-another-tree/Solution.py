# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isEqtree(self, s, t):
        if not s and not t:
            return True
        elif s and t:
            return s.val == t.val and \
                   self.isEqtree(s.left, t.left) and \
                   self.isEqtree(s.right, t.right)
        else:
            return False

    def isSubtree(self, s, t):
        if not s:
            return t is None
        elif self.isEqtree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or \
                   self.isSubtree(s.right, t)

