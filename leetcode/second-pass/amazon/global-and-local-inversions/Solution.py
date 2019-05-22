"""
Python3 solution with O(n) time and O(1) space [in-place]

I tried a couple of things before coming to the thesis that, ideal permutations
can be defined as follows:

A permutation is ideal iff it can be sorted only by reverting non overlapping
local inversions.

Might be interesting to prove mathematically that the above is equivalent
to the condition being asked here (#local inversions == #global inversions).
My thesis may actually be false, but for the moment I am happy with passing all
test cases.

If one assumes the above thesis is correct, then we can simply apply that
technique to the array and do the swaps for the non overlapping local
inversions. If after having done that we end up with a sorted array, then we
can conclude the permutation was ideal.
"""

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
