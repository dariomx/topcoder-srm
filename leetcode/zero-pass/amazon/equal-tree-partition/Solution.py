"""
Recursive Python3 solution with linear complexity

We give two passes to the nodes: first, using recursive method
we compute the sums for all the nodes. On a second pass we look
for a node whose sum is half the total, discarding the root (as
root does not have an incoming edge like the rest).
"""

class Solution:
    def checkEqualTree(self, root):
        tsum = dict()

        def calc_sum(root):
            if root is None:
                return 0
            else:
                root_sum = root.val + \
                           calc_sum(root.left) + calc_sum(root.right)
                tsum[root] = root_sum
                return root_sum

        root_sum = calc_sum(root)
        for (n, s) in tsum.items():
            if n != root and 2 * s == root_sum:
                return True
        return False
