from bisect import bisect_left
from math import inf


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def binSearch(self, mat, row, ncols, x):
        ix = -1
        start, end = 0, ncols - 1
        while start <= end:
            mid = (start + end) // 2
            y = mat.get(row, mid)
            if x <= y:
                if x == y:
                    ix = mid
                end = mid - 1
            else:
                start = mid + 1
        return ix

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ans = -1
        n, m = binaryMatrix.dimensions()
        for i in range(n):
            j = self.binSearch(binaryMatrix, i, m, 1)
            if j >= 0 and (ans < 0 or j < ans):
                ans = j
        return ans
