
class Solution:
    def findTilt(self, root):
        def rec(node):
            if node is None:
                return 0, 0
            else:
                sum_l, tilt_l = rec(node.left)
                sum_r, tilt_r = rec(node.right)
                return sum_l + node.val + sum_r, \
                       abs(sum_l - sum_r) + tilt_l + tilt_r
        return rec(root)[1]