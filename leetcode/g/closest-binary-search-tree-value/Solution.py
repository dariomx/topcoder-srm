from sys import maxint


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root:
            dist = abs(root.val - target)
            if dist == 0:
                return root.val
            else:
                ans = root.val
                left_ans = self.closestValue(root.left, target)
                left_dist = abs(left_ans - target)
                if left_dist < dist:
                    ans = left_ans
                    dist = left_dist
                right_ans = self.closestValue(root.right, target)
                right_dist = abs(right_ans - target)
                if right_dist < dist:
                    ans = right_ans
                return ans
        else:
            return maxint
