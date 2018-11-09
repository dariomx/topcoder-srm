class Solution:
    def peakIndexInMountainArray(self, A):
        start, end = 0, len(A) - 1
        while True:
            i = (start + end) // 2
            if A[i - 1] < A[i] > A[i + 1]:
                return i
            elif A[i - 1] < A[i] < A[i + 1]:
                start = i
            else:
                end = i
