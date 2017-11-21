# this is naive approach of O(n*log(n)), by simply
# defining a custom comparator and leverage standard
# sorting routine.

from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hist = defaultdict(lambda: 0)
        for c in s:
            hist[c] += 1
        return ''.join(sorted(s, key=lambda c: (-hist[c], c)))