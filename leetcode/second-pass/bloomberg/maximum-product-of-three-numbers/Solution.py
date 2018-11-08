from bisect import insort
from itertools import combinations as comb


class Solution:
    def maximumProduct(self, nums):
        k = 3
        n = len(nums)
        big = []
        small = []

        def ins(A, x, trunc=k):
            insort(A, x)
            del A[trunc:]

        for x in nums:
            ins(big, -x)
            ins(small, x)
        big = [-x for x in big]
        if n < 2 * k:
            del small[-(2 * k - n):]
        return max(x * y * z for (x, y, z) in comb(big + small, k))
