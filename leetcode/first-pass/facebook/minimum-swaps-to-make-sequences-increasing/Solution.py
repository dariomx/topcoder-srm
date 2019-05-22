# adjusted from editorial solution and discussion forum
# (could not really get this one myself, the duality of the
# DP killed me)

from sys import maxsize as maxint


class Solution:
    def minSwap(self, A, B):
        n = len(A)
        if n < 2:
            return 0
        swap_one = lambda i: A[i] < B[i + 1] and B[i] < A[i + 1]
        swap2_or_none = lambda i: A[i] < A[i + 1] and B[i] < B[i + 1]
        min_noswap, min_swap = 0, 1
        for i in range(n - 2, -1, -1):
            noswap, swap = maxint, maxint
            if swap_one(i):
                noswap = min(noswap, min_swap)
                swap = min(swap, min_noswap + 1)
            if swap2_or_none(i):
                noswap = min(noswap, min_noswap)
                swap = min(swap, min_swap + 1)
            min_noswap, min_swap = noswap, swap
        return min(min_noswap, min_swap)

