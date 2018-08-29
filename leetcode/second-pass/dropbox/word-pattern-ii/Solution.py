"""
Number Theory + Backtracking Solution

I used a backtracking solution as everybody else, but I put a little
optimization upfront. If we count the occurrences of variables in the
pattern and name k_i the counter for i-th pattern variable, we have the
following linear Diphantine equation:

k_1 * s_1 + k_2 * s_2 + ... + k_m * s_m = len(str)

where s_i is the actual length in str, of variable i-th in pattern. The
unknowns in this equation are the s_i, and we know they exist iff

gcd(k_1, k_2, ... , k_m) | len(str)

in other words, if the gcd of pattern histogram divides total length of the
string. Hence we check this upfront, and only apply the more expensive
backtracking algorithm for cases where we know solution exists.

Note: My backtracking solution may not be the best one, as I can see that I
am only at 70% of performance ranking.

"""

from math import gcd
from collections import Counter
from functools import reduce


class Solution:
    def solve(self, pat, str, asg, used, cnt):
        if not pat and not str:
            return True
        elif (not pat) != (not str):
            return False
        else:
            p = pat[0]
            if p in asg:
                psize = len(asg[p])
                pval = str[:psize]
                if pval == asg[p]:
                    return self.solve(pat[1:], str[psize:],
                                      asg, used, cnt)
                else:
                    return False
            else:
                for psize in range(1, len(str) // cnt[p] + 1):
                    pval = str[:psize]
                    if pval in used:
                        continue
                    used.add(pval)
                    asg[p] = pval
                    if self.solve(pat[1:], str[psize:],
                                  asg, used, cnt):
                        return True
                    used.remove(pval)
                    del asg[p]
                return False

    def has_soln(self, pattern, str):
        cnt = Counter(pattern)
        k = reduce(gcd, cnt.values())
        return len(str) % k == 0, cnt

    def wordPatternMatch(self, pattern, str):
        n = len(str)
        m = len(pattern)
        if 0 in (n, m):
            return n == m
        has_soln, cnt = self.has_soln(pattern, str)
        if has_soln:
            return self.solve(pattern, str, dict(), set(), cnt)
        else:
            return False

