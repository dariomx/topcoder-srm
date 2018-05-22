"""
Python3 solution with O(n) space and O(m) time

We just save all the jewel types in a set for fast query, and then iterate over
the string looking up each character in such set. Assuming that n = len(J),
m = len(S), and that n < m, then time complexity will be O(m); at the cost
of having used O(n) extra memory.
"""

class Solution:
    def numJewelsInStones(self, J, S):
        J = set(J)
        num = 0
        for c in S:
            if c in J:
                num += 1
        return num
