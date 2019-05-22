from math import gcd
from collections import Counter
from functools import reduce


class Solution:
    def accel_asc(self, n):
        a = [0 for i in range(n + 1)]
        k = 1
        y = n - 1
        while k != 0:
            x = a[k - 1] + 1
            k -= 1
            while 2 * x <= y:
                a[k] = x
                y -= x
                k += 1
            l = k + 1
            while x <= y:
                a[k] = x
                a[l] = y
                yield a[:k + 2]
                x += 1
                y -= 1
            a[k] = x + y
            y = x + y - 1
            yield a[:k + 1]

    def good_soln(self, soln, cnt):
        if len(soln) != len(cnt):
            return False
        for i in range(len(soln)):
            if soln[i] % cnt[i] != 0:
                return False
        return True

    def wordPatternMatch(self, pattern, str):
        n = len(str)
        m = len(pattern)
        if 0 in (n, m):
            return n == m
        cnt = Counter(pattern)
        k = reduce(gcd, cnt.values())
        if n % k != 0:
            return False
