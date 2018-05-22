# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Integer:
    def __init__(self, val):
        self.val = val

    def incr(self):
        self.val += 1


class Solution(object):
    def get_kth(self, node, i, k):
        if node:
            left_ret = self.get_kth(node.left, i, k)
            if left_ret is None:
                i.incr()
                if i.val == k:
                    return node.val
            else:
                return left_ret
            return self.get_kth(node.right, i, k)
        else:
            return None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.get_kth(root, Integer(0), k)
