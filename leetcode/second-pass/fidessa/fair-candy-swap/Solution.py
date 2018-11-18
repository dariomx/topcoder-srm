class Solution:
    def fairCandySwap(self, A, B):
        sA = sum(A)
        sB = sum(B)
        A2 = {2 * a for a in A}
        for b in B:
            key = sA - sB + 2 * b
            if key in A2:
                return [key // 2, b]

