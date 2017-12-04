from sys import maxint


class Solution(object):
    def solve(self, A, B, start, cache):
        if start not in cache:
            if A[start] < 0:
                cache[start] = (maxint, [])
            elif start == len(A) - 1:
                cache[start] = (0, [start + 1])
            else:
                min_coins, min_path = maxint, []
                for i in xrange(start + 1, min(start + B, len(A) - 1) + 1):
                    coins, path = self.solve(A, B, i, cache)
                    if coins < min_coins:
                        min_coins, min_path = coins, path
                    elif coins == min_coins:
                        min_path = min(min_path, path)
                if min_coins == maxint:
                    cache[start] = (maxint, [])
                else:
                    cache[start] = (
                    A[start] + min_coins, [start + 1] + min_path)
        return cache[start]

    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        return self.solve(A, B, 0, dict())[1]
