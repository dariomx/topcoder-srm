# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def max_depth(self, root):
        if root is None:
            return 0
        else:
            if root.left:
                left_depth = 1 + self.max_depth(root.left)
            else:
                left_depth = 0
            if root.right:
                right_depth = 1 + self.max_depth(root.right)
            else:
                right_depth = 0
            return max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            if root.left:
                left_depth = 1 + self.max_depth(root.left)
            else:
                left_depth = 0
            if root.right:
                right_depth = 1 + self.max_depth(root.right)
            else:
                right_depth = 0
            return left_depth + right_depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))