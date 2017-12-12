from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.shift_tab = dict()
        for i in xrange(ord('a'), ord('z')):
            self.shift_tab[chr(i)] = chr(i + 1)
        self.shift_tab['z'] = 'a'

    def shift(self, s):
        ss = ''
        for c in s:
            ss += self.shift_tab[c]
        return ss

    def reduce(self, start):
        s = start
        canon = s
        while True:
            ss = self.shift(s)
            if ss == start:
                break
            else:
                s = ss
                canon = min(canon, s)
        return canon

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for s in strings:
            groups[self.reduce(s)].append(s)
        return groups.values()
