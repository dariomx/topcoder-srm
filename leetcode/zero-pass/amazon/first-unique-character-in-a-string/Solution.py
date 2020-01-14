"""
Python3 solution with O(n) time and O(1) space

The main piece of information we can leverage, is the known range of
characters of the string (a-z). Using this info we can create a couple of
small arrays, indexed by ascii code, in order to track both counter of
occurrences and last position seen.

Then we iterate once over the string, updating these two arrays. After that,
we just go over the small arrays and compute the minimum position across all
characters with a counter==1.
"""

class Solution:
    def firstUniqChar(self, s):
        n = len(s)
        m = ord('z') - ord('a') + 1
        shift = ord('a')
        cnt = [0] * m
        pos = [0] * m
        for i in range(n):
            k = ord(s[i]) - shift
            cnt[k] += 1
            pos[k] = i
        fpos = n
        for i in range(m):
            if cnt[i] == 1 and pos[i] < fpos:
                fpos = pos[i]
        return -1 if fpos == n else fpos
