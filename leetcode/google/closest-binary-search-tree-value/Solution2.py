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
        closest = None
        min_dist = maxint
        stack = [root]
        while stack:
            node = stack.pop()
            dist = abs(node.val - target)
            if dist < min_dist:
                min_dist = dist
                closest = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return closest
