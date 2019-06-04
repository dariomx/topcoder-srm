from math import inf


class Solution(object):
    def __init__(self):
        self.max_from = {None: 0}

    def maxPathSum(self, root):
        if root is None:
            return -inf
        else:
            max_left = self.maxPathSum(root.left)
            max_right = self.maxPathSum(root.right)
            from_left = self.max_from.get(root.left, 0)
            from_right = self.max_from.get(root.right, 0)
            self.max_from[root] = max(root.val,
                                      root.val + max(from_left, from_right))
            return max(max_left, max_right, root.val,
                       root.val + from_left, root.val + from_right,
                       root.val + from_left + from_right)
