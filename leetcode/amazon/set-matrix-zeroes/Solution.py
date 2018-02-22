"""
Easy to understand Python3 with O(n) space and time

Every position (i,j) in modified matrix will be zero, if there was any zero
on either row i-th or column j-th. We give a first pass in order to compute
that information, and then do a second pass to assign all cells based on such
rule.

After looking at the phorum, realized that there is no need to create the two
new arrays (which btw, should be faster than hash-tables). One can use the
first column and row to store that information.
"""

class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        zerorow = [False] * m
        zerocol = [False] * n
        for i in range(m):
            for j in range(n):
                is_zero = (matrix[i][j] == 0)
                zerorow[i] = zerorow[i] or is_zero
                zerocol[j] = zerocol[j] or is_zero
        for i in range(m):
            for j in range(n):
                if zerorow[i] or zerocol[j]:
                    matrix[i][j] = 0