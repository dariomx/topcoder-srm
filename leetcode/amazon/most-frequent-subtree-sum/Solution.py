"""
Recursive Python3 solution, beats them all.

We compute first, recursively, the sum for each node and save it into a dict.
Then we iterate over the dict once and compute both the maximum frequency and
the associated list of sums.

Space complexity is O(n) due sum_nodes dict, and time should be O(n) I guess?
(cause the recursion touches just once every node).
"""

from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root):
        sum_nodes = defaultdict(lambda: 0)

        def rec(node):
            if node:
                left = rec(node.left)
                right = rec(node.right)
                s = node.val + left + right
                sum_nodes[s] += 1
                return s
            else:
                return 0

        rec(root)
        maxc = 0
        ret = []
        for s, c in sum_nodes.items():
            if c > maxc:
                maxc = c
                ret = [s]
            elif c == maxc:
                ret.append(s)
        return ret


