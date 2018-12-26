class Solution:
    def validMountainArray(self, A):
        n = len(A)
        if n < 3:
            return False
        start, end = 0, n - 1
        cand = False
        while end - start + 1 >= 3:
            mid = (start + end) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                cand = True
                break
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        if cand:
            for i in range(mid):
                if A[i] >= A[i + 1]:
                    return False
            for i in range(mid, n - 1):
                if A[i] <= A[i + 1]:
                    return False
            return True
        else:
            return False

