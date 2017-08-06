# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def calc_rows(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.calc_rows(root.left), self.calc_rows(root.right))

    def calc_cols(self, root):
        if root is None:
            return 0
        else:
            return 1 + 2 * max(self.calc_cols(root.left), self.calc_cols(root.right))

    def print_tree(self, root, scr, row, start, end):
        if root is not None:
            mid = (start + end) / 2
            scr[row][mid] = str(root.val)
            self.print_tree(root.left, scr, row + 1, start, mid - 1)
            self.print_tree(root.right, scr, row + 1, mid + 1, end)

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        n, m = self.calc_rows(root), self.calc_cols(root)
        scr = [[''] * m for _ in xrange(n)]
        self.print_tree(root, scr, 0, 0, m - 1)
        return scr
