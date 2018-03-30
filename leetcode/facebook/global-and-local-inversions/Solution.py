class Solution:
    def isIdealPermutation(self, A):
        n = len(A)
        i = 0
        while i < n - 1:
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                i += 1
            i += 1
        for i in range(n):
            if i != A[i]:
                return False
        return True
