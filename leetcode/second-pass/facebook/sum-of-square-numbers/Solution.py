from math import sqrt


class Solution:
    def judgeSquareSum(self, c):
        S = {x * x for x in range(int(sqrt(c)) + 1)}
        for y in S:
            if c - y in S:
                return True
        return False
