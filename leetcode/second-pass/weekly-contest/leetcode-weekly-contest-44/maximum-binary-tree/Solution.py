# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sys import maxint


class Solution(object):
    def get_max_idx(self, arr, start, end):
        max_x, max_i = -maxint, -1
        for i in xrange(start, end + 1):
            x = arr[i]
            if x > max_x:
                max_x = x
                max_i = i
        return max_i

    def build_tree(self, arr, start, end):
        if start > end:
            return None
        else:
            max_i = self.get_max_idx(arr, start, end)
            root = TreeNode(arr[max_i])
            root.left = self.build_tree(arr, start, max_i - 1)
            root.right = self.build_tree(arr, max_i + 1, end)
            return root

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(nums, 0, len(nums) - 1)
