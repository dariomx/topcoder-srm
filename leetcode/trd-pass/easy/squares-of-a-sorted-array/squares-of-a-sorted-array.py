class Solution:
    def merge(self, A, B):
        C = []
        n, m = len(A), len(B)
        i, j = n - 1, 0
        while i >= 0 and j < m:
            if A[i] == B[j]:
                C.append(A[i])
                C.append(B[j])
                i -= 1
                j += 1
            elif A[i] < B[j]:
                C.append(A[i])
                i -= 1
            else:
                C.append(B[j])
                j += 1
        if i >= 0:
            C += A[:(i + 1)][::-1]
        elif j < m:
            C += B[j:]
        return C

    def sortedSquares(self, A: List[int]) -> List[int]:
        negSq = []
        posSq = []
        for x in A:
            if x < 0:
                negSq.append(x ** 2)
            else:
                posSq.append(x ** 2)
        return self.merge(negSq, posSq)
