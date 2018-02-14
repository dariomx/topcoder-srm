"""
Five-lines Python3 solution with O(n) time

If the words are anagram of each other, then their character histograms
are the same. We leverage new Counter class in Python3.
"""

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)