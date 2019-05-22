class Solution:
    def sortArrayByParityII(self, A):
        A.sort(key=lambda x: x % 2)
        n = len(A)
        half = n // 2
        j = half + half % 2
        for i in range(1, half, 2):
            A[i], A[j] = A[j], A[i]
            j += 2
        return A
