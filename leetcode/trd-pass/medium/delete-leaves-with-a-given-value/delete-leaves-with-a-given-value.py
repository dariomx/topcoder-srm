class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def canRemove(n):
            return n and n.left is None and n.right is None and n.val == target

        if root:
            self.removeLeafNodes(root.left, target)
            if canRemove(root.left):
                root.left = None
            self.removeLeafNodes(root.right, target)
            if canRemove(root.right):
                root.right = None
            if canRemove(root):
                root = None
        return root
