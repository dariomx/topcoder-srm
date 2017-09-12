# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def max_depth(self, root, depth):
        if root is None:
            return depth
        else:
            if root.left:
                left_depth = self.max_depth(root.left, depth + 1)
            else:
                left_depth = depth
            if root.right:
                right_depth = self.max_depth(root.right, depth + 1)
            else:
                right_depth = depth
            return max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self.max_depth(root.left, 1) + \
                   self.max_depth(root.right, 1)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))