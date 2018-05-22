"""
This is a semi-brute force approach, where I insisted that the key was to use
binary search in either row or column. It only passes in Python3. I think
the complexity in worst case is O(k * log(k)), where k = max(n, m)
"""

from collections import defaultdict

ROW = 1
COL = 2


class Solution:
    def binSearchRow(self, i, mat, x):
        m = len(mat[i])
        start = 0
        end = m - 1
        mid = None
        while start <= end:
            mid = (start + end) // 2
            if mat[i][mid] == x:
                return (True, mid)
            elif x < mat[i][mid]:
                end = mid - 1
            else:
                start = mid + 1
        return (False, mid)

    def binSearchCol(self, j, mat, x):
        n = len(mat)
        start = 0
        end = n - 1
        mid = None
        while start <= end:
            mid = (start + end) // 2
            if mat[mid][j] == x:
                return (True, mid)
            elif x < mat[mid][j]:
                end = mid - 1
            else:
                start = mid + 1
        return (False, mid)

    def searchMatrix(self, mat, x):
        m = len(mat)
        if m == 0:
            return False
        n = len(mat[0])
        if n == 0:
            return False
        used = defaultdict(lambda: set())
        stack = [(ROW, m // 2)]
        while stack:
            print(stack)
            typ, k = stack.pop()
            if k in used[typ]:
                continue
            used[typ].add(k)
            if typ == ROW:
                found, mid = self.binSearchRow(k, mat, x)
                if found:
                    return True
                else:
                    if (0 <= mid - 1 < n):
                        stack.append((COL, mid - 1))
                    stack.append((COL, mid))
                    if (0 <= mid + 1 < n):
                        stack.append((COL, mid + 1))
            else:
                found, mid = self.binSearchCol(k, mat, x)
                if found:
                    return True
                else:
                    if (0 <= mid - 1 < m):
                        stack.append((ROW, mid - 1))
                    stack.append((ROW, mid))
                    if (0 <= mid + 1 < m):
                        stack.append((ROW, mid + 1))
        return False
