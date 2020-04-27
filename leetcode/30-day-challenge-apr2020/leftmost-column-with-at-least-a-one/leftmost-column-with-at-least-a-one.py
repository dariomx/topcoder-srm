from bisect import bisect_left


class Solution:
    def searchOne(self, mat, row, in_end):
        start, end = 0, in_end
        while start <= end:
            mid = (start + end) // 2
            if mat.get(row, mid) == 1:
                if mid == 0 or mat.get(row, mid - 1) == 0:
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
        return in_end + 1

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        end = m - 1
        ans = m
        for i in range(n):
            j = self.searchOne(binaryMatrix, i, end)
            ans = min(ans, j)
            end = min(end, j)
            if ans == 0:
                break
        return -1 if ans == m else ans