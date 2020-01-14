"""
Python3 solution with O(1) space and O(n) time

We use the canonical in-place algorithm for reversing strings, where position
i-th gets swapped with position n-i-1. Then use that routine to reverse whole
string, and by doing that we will have proper word order.

A second pass is needed to reverse within the boundaries, in order to put the
words on the original order.
"""

class Solution:
    def reverse(self, str, start, end):
        n = end - start + 1
        for i in range(start, start + n // 2):
            j = end - (i - start)
            str[i], str[j] = str[j], str[i]
        return str

    def reverseWords(self, str):
        n = len(str)
        self.reverse(str, 0, n - 1)
        start = end = 0
        for i in range(n):
            if str[i] == ' ':
                self.reverse(str, start, end)
                start = end = i + 1
            else:
                end = i
        if start < end:
            self.reverse(str, start, end)
