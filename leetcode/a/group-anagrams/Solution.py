"""
This had a trivial solution, but I forgot how to hash strings (aka, the tuple trick). Hence I came up with an encoding for each string: starting for the canonical representation (sorted string), I encode each character as a "digit" on a  number system with base = ord('z) - ord('a').
"""

from collections import defaultdict

class Solution(object):
    def key(self, s):
        base = ord('z') - ord('a')
        k = 0
        pow = 1
        for c in sorted(s):
            k += pow * (ord(c) - ord('a'))
            pow *= base
        return k

    def groupAnagrams(self, strs):
        groups = defaultdict(lambda: [])
        for s in strs:
            groups[self.key(s)].append(s)
        return groups.values()