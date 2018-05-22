"""
Python3 generic solution with single loop.

We use generic algorithm for adding large numbers in arbitrary base. The loop
considers the 3 possible cases (both arrays are still aligned, or we finish
one of them). As we traverse them once, time complexity is O(n + m), where
n = len(a) and m = len(b).
"""

class Solution:
    def addBinary(self, a, b):
        base = 2
        i = len(a) - 1
        j = len(b) - 1
        ans = ""
        rem = 0
        while i >= 0 or j >= 0:
            x = rem
            if i >= 0:
                x += int(a[i])
                i -= 1
            if j >= 0:
                x += int(b[j])
                j -= 1
            ans = str(x % base) + ans
            rem = x // base
        if rem > 0:
            ans = str(rem) + ans
        return ans

