"""
Python3 solution with divisibility trick.

I could not really figure out a more elegant way, but here it is:

1) First of all, if string is a repeated substring then such substring must
be at the beginning.

2) If we knew in advance what is the length of this substring, let us say k,
then we could check in linear time whether the string is really a repeated
version of it.

3) Whatever value k has, it must be the case that n = k * rep, where n = len(s)
and rep is the number of times the substring repeats. This implies,
in particular, that n must be divisible by rep.

4) Using the conclusion from #3, we search for all possible values of rep and
only those passing the division test get tested in O(n), as we mention in #2.
"""

class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for rep in range(2, n + 1):
            if n % rep == 0:
                found = True
                k = n // rep
                for i in range(k, n):
                    if s[i] != s[i % k]:
                        found = False
                        break
                if found:
                    return True
        return False
